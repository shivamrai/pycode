# -- coding: utf-8 --
"""
Created on Tue May 14 11:00:08 2019

@author: NIKHIT
"""

# Importing required libraries
from sklearn.svm import SVC
import sqlite3
import pandas as pd
import numpy as np
from time import time
import seaborn as sns

# import itertools
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error

# from sklearn.preprocessing import LabelEncoder as le
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import cross_val_score


def get_match_label(match):
    """Derives a label for a given match."""

    # Define variables
    home_goals = match["home_team_goal"]
    away_goals = match["away_team_goal"]

    label = pd.DataFrame()
    label.loc[0, "match_api_id"] = match["match_api_id"]

    # Identify match label
    if home_goals > away_goals:
        label.loc[0, "label"] = "Win"
    if home_goals == away_goals:
        label.loc[0, "label"] = "Draw"
    if home_goals < away_goals:
        label.loc[0, "label"] = "Defeat"

    # Return label
    return label.loc[0]


def get_fifa_stats(match, player_stats):
    """Aggregates fifa stats for a given match."""

    # Define variables
    match_id = match.match_api_id
    date = match["date"]
    players = [
        "home_player_1",
        "home_player_2",
        "home_player_3",
        "home_player_4",
        "home_player_5",
        "home_player_6",
        "home_player_7",
        "home_player_8",
        "home_player_9",
        "home_player_10",
        "home_player_11",
        "away_player_1",
        "away_player_2",
        "away_player_3",
        "away_player_4",
        "away_player_5",
        "away_player_6",
        "away_player_7",
        "away_player_8",
        "away_player_9",
        "away_player_10",
        "away_player_11",
    ]
    player_stats_new = pd.DataFrame()
    names = []

    # Loop through all players
    for player in players:

        # Get player ID
        player_id = match[player]

        # Get player stats
        stats = player_stats[player_stats.player_api_id == player_id]

        # Identify current stats
        current_stats = stats[stats.date < date].sort_values(by="date", ascending=False)[:1]

        if np.isnan(player_id):
            overall_rating = pd.Series(0)
        else:
            current_stats.reset_index(inplace=True, drop=True)
            overall_rating = pd.Series(current_stats.loc[0, "overall_rating"])

        # Rename stat
        name = "{}_overall_rating".format(player)
        names.append(name)

        # Aggregate stats
        player_stats_new = pd.concat([player_stats_new, overall_rating], axis=1)

    player_stats_new.columns = names
    player_stats_new["match_api_id"] = match_id

    player_stats_new.reset_index(inplace=True, drop=True)

    # Return player stats
    # return player_stats_new.ix[0]
    return player_stats_new.loc[0]


def get_fifa_data(matches, player_stats, path=None, data_exists=False):
    """Gets fifa data for all matches."""

    # Check if fifa data already exists
    if data_exists:

        fifa_data = pd.read_pickle(path)

    else:

        print("Collecting fifa data for each match...")
        start = time()

        # Apply get_fifa_stats for each match
        fifa_data = matches.apply(lambda x: get_fifa_stats(x, player_stats), axis=1)

        end = time()
        print("Fifa data collected in {:.1f} minutes".format((end - start) / 60))

    # Return fifa_data
    return fifa_data


def convert_odds_to_prob(match_odds):
    """Converts bookkeeper odds to probabilities."""

    # Define variables
    match_id = match_odds.loc[:, "match_api_id"]
    bookkeeper = match_odds.loc[:, "bookkeeper"]
    win_odd = match_odds.loc[:, "Win"]
    draw_odd = match_odds.loc[:, "Draw"]
    loss_odd = match_odds.loc[:, "Defeat"]

    # Converts odds to prob
    win_prob = 1 / win_odd
    draw_prob = 1 / draw_odd
    loss_prob = 1 / loss_odd

    total_prob = win_prob + draw_prob + loss_prob

    probs = pd.DataFrame()

    # Define output format and scale probs by sum over all probs
    probs.loc[:, "match_api_id"] = match_id
    probs.loc[:, "bookkeeper"] = bookkeeper
    probs.loc[:, "Win"] = win_prob / total_prob
    probs.loc[:, "Draw"] = draw_prob / total_prob
    probs.loc[:, "Defeat"] = loss_prob / total_prob

    # Return probs and meta data
    return probs


def get_bookkeeper_data(matches, bookkeepers, horizontal=True):
    """Aggregates bookkeeper data for all matches and bookkeepers."""

    bk_data = pd.DataFrame()

    # Loop through bookkeepers
    for bookkeeper in bookkeepers:

        # Find columns containing data of bookkeeper
        temp_data = matches.loc[:, (matches.columns.str.contains(bookkeeper))]
        temp_data.loc[:, "bookkeeper"] = str(bookkeeper)
        temp_data.loc[:, "match_api_id"] = matches.loc[:, "match_api_id"]

        # Rename odds columns and convert to numeric
        cols = temp_data.columns.values
        cols[:3] = ["Win", "Draw", "Defeat"]
        temp_data.columns = cols
        temp_data.loc[:, "Win"] = pd.to_numeric(temp_data["Win"])
        temp_data.loc[:, "Draw"] = pd.to_numeric(temp_data["Draw"])
        temp_data.loc[:, "Defeat"] = pd.to_numeric(temp_data["Defeat"])

        # Check if data should be aggregated horizontally
        if horizontal:

            # Convert data to probs
            temp_data = convert_odds_to_prob(temp_data)
            temp_data.drop("match_api_id", axis=1, inplace=True)
            temp_data.drop("bookkeeper", axis=1, inplace=True)

            # Rename columns with bookkeeper names
            win_name = bookkeeper + "_" + "Win"
            draw_name = bookkeeper + "_" + "Draw"
            defeat_name = bookkeeper + "_" + "Defeat"
            temp_data.columns.values[:3] = [win_name, draw_name, defeat_name]

            # Aggregate data
            bk_data = pd.concat([bk_data, temp_data], axis=1)
        else:
            # Aggregate vertically
            bk_data = bk_data.append(temp_data, ignore_index=True)

    # If horizontal add match api id to data
    if horizontal:
        temp_data.loc[:, "match_api_id"] = matches.loc[:, "match_api_id"]

    # Return bookkeeper data
    return bk_data


def get_overall_fifa_rankings(fifa, get_overall=False):
    """Get overall fifa rankings from fifa data."""

    temp_data = fifa

    # Check if only overall player stats are desired
    if get_overall:

        # Get overall stats
        data = temp_data.loc[:, (fifa.columns.str.contains("overall_rating"))]
        data.loc[:, "match_api_id"] = temp_data.loc[:, "match_api_id"]
    else:

        # Get all stats except for stat date
        cols = fifa.loc[:, (fifa.columns.str.contains("date_stat"))]
        temp_data = fifa.drop(cols.columns, axis=1)
        data = temp_data

    # Return data
    return data


def get_wins(matches, team):
    """Get the number of wins of a specfic team from a set of matches."""

    # Find home and away wins
    home_wins = int(
        matches.home_team_goal[
            (matches.home_team_api_id == team) & (matches.home_team_goal > matches.away_team_goal)
        ].count()
    )
    away_wins = int(
        matches.away_team_goal[
            (matches.away_team_api_id == team) & (matches.away_team_goal > matches.home_team_goal)
        ].count()
    )

    total_wins = home_wins + away_wins

    # Return total wins
    return total_wins


def get_goals(matches, team):
    """Get the goals of a specfic team from a set of matches."""

    # Find home and away goals
    home_goals = int(matches.home_team_goal[matches.home_team_api_id == team].sum())
    away_goals = int(matches.away_team_goal[matches.away_team_api_id == team].sum())

    total_goals = home_goals + away_goals

    # Return total goals
    return total_goals


def get_last_matches(matches, date, team, x=10):
    """Get the last x matches of a given team."""

    # Filter team matches from matches
    team_matches = matches[(matches["home_team_api_id"] == team) | (matches["away_team_api_id"] == team)]

    # Filter x last matches from team matches
    last_matches = team_matches[team_matches.date < date].sort_values(by="date", ascending=False).iloc[0:x, :]

    # Return last matches
    return last_matches


def get_last_matches_against_eachother(matches, date, home_team, away_team, x=10):
    """Get the last x matches of two given teams."""

    # Find matches of both teams
    home_matches = matches[(matches["home_team_api_id"] == home_team) & (matches["away_team_api_id"] == away_team)]
    away_matches = matches[(matches["home_team_api_id"] == away_team) & (matches["away_team_api_id"] == home_team)]
    total_matches = pd.concat([home_matches, away_matches])

    # Get last x matches
    try:
        last_matches = total_matches[total_matches.date < date].sort_values(by="date", ascending=False).iloc[0:x, :]
    except BaseException:
        last_matches = (
            total_matches[total_matches.date < date]
            .sort_values(by="date", ascending=False)
            .iloc[0 : total_matches.shape[0], :]
        )

        # Check for error in data
        if last_matches.shape[0] > x:
            print("Error in obtaining matches")

    # Return data
    return last_matches


def get_goals_conceided(matches, team):
    """Get the goals conceided of a specfic team from a set of matches."""

    # Find home and away goals
    home_goals = int(matches.home_team_goal[matches.away_team_api_id == team].sum())
    away_goals = int(matches.away_team_goal[matches.home_team_api_id == team].sum())

    total_goals = home_goals + away_goals

    return total_goals


def get_match_features(match, matches, x=10):
    """Create match specific features for a given match."""

    # Define variables
    date = match.date
    home_team = match.home_team_api_id
    away_team = match.away_team_api_id

    # Get last x matches of home and away team
    matches_home_team = get_last_matches(matches, date, home_team, x=10)
    matches_away_team = get_last_matches(matches, date, away_team, x=10)

    # Get last x matches of both teams against each other
    last_matches_against = get_last_matches_against_eachother(matches, date, home_team, away_team, x=3)

    # Create goal variables
    home_goals = get_goals(matches_home_team, home_team)
    away_goals = get_goals(matches_away_team, away_team)
    home_goals_conceided = get_goals_conceided(matches_home_team, home_team)
    away_goals_conceided = get_goals_conceided(matches_away_team, away_team)

    # Define result data frame
    result = pd.DataFrame()

    # Define ID features
    result.loc[0, "match_api_id"] = match.match_api_id
    result.loc[0, "league_id"] = match.league_id

    # Create match features
    result.loc[0, "home_team_goals_difference"] = home_goals - home_goals_conceided
    result.loc[0, "away_team_goals_difference"] = away_goals - away_goals_conceided
    result.loc[0, "games_won_home_team"] = get_wins(matches_home_team, home_team)
    result.loc[0, "games_won_away_team"] = get_wins(matches_away_team, away_team)
    result.loc[0, "games_against_won"] = get_wins(last_matches_against, home_team)
    result.loc[0, "games_against_lost"] = get_wins(last_matches_against, away_team)

    # Return match features
    return result.loc[0]


def create_feables(matches, fifa, bookkeepers, get_overall=False, horizontal=True, x=10, verbose=True):
    """Create and aggregate features and labels for all matches."""

    # Get fifa stats features
    fifa_stats = get_overall_fifa_rankings(fifa, get_overall)

    if verbose:
        print("Generating match features...")
    start = time()

    # Get match features for all matches
    match_stats = matches.apply(lambda x: get_match_features(x, matches, x=10), axis=1)

    # Create dummies for league ID feature
    dummies = pd.get_dummies(match_stats["league_id"]).rename(columns=lambda x: "League_" + str(x))
    match_stats = pd.concat([match_stats, dummies], axis=1)
    match_stats.drop(["league_id"], inplace=True, axis=1)

    end = time()
    if verbose:
        print("Match features generated in {:.1f} minutes".format((end - start) / 60))

    if verbose:
        print("Generating match labels...")
    start = time()

    # Create match labels
    labels = matches.apply(get_match_label, axis=1)
    end = time()
    if verbose:
        print("Match labels generated in {:.1f} minutes".format((end - start) / 60))

    if verbose:
        print("Generating bookkeeper data...")
    start = time()

    # Get bookkeeper quotas for all matches
    bk_data = get_bookkeeper_data(matches, bookkeepers, horizontal=True)
    bk_data.loc[:, "match_api_id"] = matches.loc[:, "match_api_id"]
    end = time()
    if verbose:
        print("Bookkeeper data generated in {:.1f} minutes".format((end - start) / 60))

    # Merges features and labels into one frame
    features = pd.merge(match_stats, fifa_stats, on="match_api_id", how="left")
    features = pd.merge(features, bk_data, on="match_api_id", how="left")
    feables = pd.merge(features, labels, on="match_api_id", how="left")

    # Drop NA values
    feables.dropna(inplace=True)

    # Return preprocessed data
    return feables


def explore_data(features, inputs, path):
    """Explore data by plotting KDE graphs."""

    # Define figure subplots
    fig = plt.figure(1)
    fig.subplots_adjust(bottom=-1, left=0.025, top=2, right=0.975)

    # Loop through features
    i = 1
    for col in features.columns:

        # Set subplot and plot format
        sns.set_style("darkgrid")
        sns.set_context("talk", font_scale=0.8, rc={"lines.linewidth": 2})
        plt.subplot(7, 7, 0 + i)
        j = i - 1

        # Plot KDE for all labels
        sns.distplot(inputs[inputs["label"] == "Win"].iloc[:, j], hist=False, label="Win")
        sns.distplot(inputs[inputs["label"] == "Draw"].iloc[:, j], hist=False, label="Draw")
        sns.distplot(inputs[inputs["label"] == "Defeat"].iloc[:, j], hist=False, label="Defeat")
        plt.legend()
        i = i + 1

    # Define plot format
    DefaultSize = fig.get_size_inches()
    fig.set_size_inches((DefaultSize[0] * 3.5, DefaultSize[1] * 3.5))

    plt.show()

    # Compute and print label weights
    labels = inputs.loc[:, "label"]
    class_weights = labels.value_counts() / len(labels)
    print(class_weights)

    # Store description of all features
    feature_details = features.describe().transpose()

    # Return feature details
    return feature_details


# main function to test all code


def main():
    start = time()


# Fetching data
# Connecting to database
path = path = r"C:\Users\NIKHIT\Documents\pycode\database.db"  # Insert path here
# database = path + 'database.sqlite'
conn = sqlite3.connect(path)

# Defining the number of jobs to be run in parallel during grid search
n_jobs = 1  # Insert number of parallel jobs here

# Fetching required data tables
player_data = pd.read_sql("SELECT * FROM Player;", conn)
player_stats_data = pd.read_sql("SELECT * FROM Player_Attributes;", conn)
team_data = pd.read_sql("SELECT * FROM Team;", conn)
match_data = pd.read_sql("SELECT * FROM Match;", conn)

# Reduce match data to fulfill run time requirements
rows = [
    "country_id",
    "league_id",
    "season",
    "stage",
    "date",
    "match_api_id",
    "home_team_api_id",
    "away_team_api_id",
    "home_team_goal",
    "away_team_goal",
    "home_player_1",
    "home_player_2",
    "home_player_3",
    "home_player_4",
    "home_player_5",
    "home_player_6",
    "home_player_7",
    "home_player_8",
    "home_player_9",
    "home_player_10",
    "home_player_11",
    "away_player_1",
    "away_player_2",
    "away_player_3",
    "away_player_4",
    "away_player_5",
    "away_player_6",
    "away_player_7",
    "away_player_8",
    "away_player_9",
    "away_player_10",
    "away_player_11",
]
match_data.dropna(subset=rows, inplace=True)
match_data = match_data.tail(1500)
# fifa_stats=get_fifa_stats(match_data, player_stats_data)
# Generating features, exploring the data, and preparing data for model training
# Generating or retrieving already existant FIFA data
fifa_data = get_fifa_data(match_data, player_stats_data, data_exists=False)

# Creating features and labels based on data provided
bk_cols = ["B365", "BW", "IW", "LB", "PS", "WH", "SJ", "VC", "GB", "BS"]
bk_cols_selected = ["B365", "BW"]
feables = create_feables(match_data, fifa_data, bk_cols_selected, get_overall=True)
inputs = feables.drop("match_api_id", axis=1)
sns.heatmap(feables.corr())

# Exploring the data and creating visualizations
labels = inputs.loc[:, "label"]
features = inputs.drop("label", axis=1)
features.head(5)
feature_details = explore_data(features, inputs, path)
# getting bookkeeperdata
bk_data = pd.DataFrame()
bk_data = get_bookkeeper_data(match_data, bk_cols_selected, horizontal=True)
print(bk_data)
# Split our data
train, test, train_labels, test_labels = train_test_split(features, labels, test_size=0.45, random_state=42)

gnb = GaussianNB()
model = gnb.fit(train, train_labels)
# Make predictions
preds = gnb.predict(test)
print(preds)

print(accuracy_score(test_labels, preds))
for column in feables.columns:
    if feables[column].dtype == type(object):
        le = preprocessing.LabelEncoder()
        feables[column] = le.fit_transform(feables[column])

X = feables.drop(["label"], axis=1).values
# Y=feables.('label')
y = feables.filter(["label"]).values
# knn = KNeighborsClassifier()

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0, random_state=0)


# for i in range(0,60):
#     print("Error in value number",i,(X[i]-y[i]))
#     time.sleep(1)


# Split our data
train, test, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=42)


gnb = GaussianNB()
model = gnb.fit(train, train_labels)
# Make predictions
preds = gnb.predict(test)
print(preds)

print(accuracy_score(test_labels, preds))
# print(mean_squared_error(X, y))
# mean_squared_error(X, y)

# combined rmse value
KNN_clf = KNeighborsClassifier()
model = KNN_clf.fit(train, train_labels)
preds = KNN_clf.predict(test)
print(preds)
print(accuracy_score(test_labels, preds))

# rss=((X-y)**2).sum()
# mse=np.mean((X-y)**2)
# print("Final rmse value is =",np.sqrt(np.mean((X-y)**2)))

AB_clf = AdaBoostClassifier(n_estimators=300, random_state=2)
model = AB_clf.fit(train, train_labels)
preds = AB_clf.predict(test)
print(preds)
print(accuracy_score(test_labels, preds))


LOG_clf = linear_model.LogisticRegression(multi_class="ovr", solver="sag", class_weight="balanced")
model = LOG_clf.fit(train, train_labels)
preds = LOG_clf.predict(test)
print(preds)
print(accuracy_score(test_labels, preds))

R_F = RandomForestClassifier(n_estimators=300, max_depth=3, random_state=2)
model = R_F.fit(train, train_labels)
preds = R_F.predict(test)
print(preds)
print(accuracy_score(test_labels, preds))
scores = []
num_features = len(train.columns)
for i in range(num_features):
    col = train.columns[i]
    score = np.mean(cross_val_score(R_F, X[col].values.reshape(-1, 1), y, cv=10))
    scores.append((int(score * 100), col))

print(sorted(scores, reverse=True))


svclassifier = SVC(kernel="linear")
model = svclassifier.fit(train, train_labels)
preds = svclassifier.predict(test)
print(preds)
print(accuracy_score(test_labels, preds))

if _name_ == "_main_":
    # execute only if run as a script
    main()
