#!/usr/bin/env python3
"""Comprehensive automation script to refactor Python files for PEP8 compliance."""

import os
import re
from pathlib import Path

# Problem descriptions mapped to filenames
PROBLEM_DESCRIPTIONS = {
    "alternative_foo_bar.py": "Alternative Foo Bar - Print Foo and Bar in alternating pattern",
    "applesandoranges.py": "Apples and Oranges - Count fruits within distance ranges",
    "arranging_coins.py": "Arranging Coins - Determine rows in staircase",
    "array_pairs.py": "Array Pairs - Check if array can be divided into pairs divisible by 60",
    "arrival_departure.py": "Platform for Trains - Find minimum platforms needed",
    "baseball.py": "Baseball Game - Calculate score with special operations",
    "binary_ones.py": "Count Binary Substrings - Count consecutive ones and zeros",
    "canplaceflowers.py": "Can Place Flowers - Check if flowers can be planted",
    "closest_number.py": "Closest Numbers - Find pair with smallest difference",
    "coinchange.py": "Coin Change - Find minimum coins for target amount",
    "combination.py": "Divisible by 3 - Check if list sum divisible by 3",
    "construct_tree.py": "Construct Binary Tree - Build tree from traversals",
    "count_binary_strs.py": "Count Binary Substrings - Find consecutive equal character groups",
    "decode_at_index.py": "Decode String at Index - Find character at decoded position",
    "dictionary_file_reading.py": "Dictionary File Reading - Process dictionary file",
    "drawingmatrix.py": "Drawing Matrix - Create matrix pattern",
    "duplicate_zeros.py": "Duplicate Zeros - Duplicate each zero in array",
    "factorial.py": "Factorial - Calculate factorial of a number",
    "filestowordlist.py": "Files to Word List - Convert file to word list",
    "finalproject.py": "Final Project - Machine learning classification project",
    "getmaximumgenerated.py": "Get Maximum Generated - Find maximum in generated sequence",
    "grader.py": "Grader - Grade assignment submissions",
    "hextodec.py": "Hex to Decimal - Convert hexadecimal to decimal",
    "hourglass.py": "2D Array Hourglass - Find maximum hourglass sum",
    "inheritence.py": "Inheritance - Demonstrate class inheritance",
    "inordertree.py": "Level Order Tree Traversal - Traverse tree by levels",
    "insertionsort.py": "Insertion Sort - Sort array using insertion sort algorithm",
    "invert_tree.py": "Invert Binary Tree - Mirror a binary tree",
    "is_symmetric_tree.py": "Symmetric Tree - Check if tree is symmetric",
    "items.py": "Items - Process items collection",
    "jump_game.py": "Jump Game - Determine if reachable end of array",
    "kthfactorofn.py": "Kth Factor - Find kth smallest factor of n",
    "length_of_longest_substring.py": "Longest Substring Without Repeating Characters",
    "linked_list_doubly.py": "Doubly Linked List - Implement doubly linked list",
    "linkedlist.py": "Linked List - Implement singly linked list operations",
    "listmndeletion.py": "List Manipulation and Deletion - Delete elements from list",
    "listprimes.py": "List Primes - Generate list of prime numbers",
    "longest_subtring_without.py": "Longest Substring Without Repeating - Find longest unique substring",
    "l_r_u_cache.py": "LRU Cache - Implement Least Recently Used cache",
    "matrixsum.py": "Matrix Sum - Calculate sum of matrix elements",
    "max_ascending_sum.py": "Maximum Ascending Subarray Sum - Find max sum of increasing subarray",
    "max_depth_binary_tree.py": "Maximum Depth Binary Tree - Find maximum depth of tree",
    "max_distance.py": "Maximum Distance - Find maximum distance between elements",
    "max_distbtw2samechars.py": "Max Distance Between Same Characters",
    "max_frequenct_stack.py": "Maximum Frequency Stack - Stack with max frequency element",
    "max_profit_shares.py": "Max Profit Shares - Calculate maximum profit from stocks",
    "max_sub_array.py": "Maximum Subarray - Find largest sum of contiguous subarray",
    "max_time.py": "Maximum Time - Find valid time with maximum hour/minute",
    "maxdifflarge.py": "Max Difference - Find maximum difference in array",
    "maximum_frequency_stack.py": "Maximum Frequency Stack - Stack with max frequency element",
    "merge2_sorted_linked_lists.py": "Merge Sorted Lists - Merge two sorted linked lists",
    "merge_lists.py": "Merge Lists - Merge multiple lists",
    "merge_sorted.py": "Merge Sorted Array - Merge two sorted arrays",
    "min_sub_sum.py": "Minimum Subarray Sum - Find minimum sum of contiguous subarray",
    "minmaxsum.py": "Min-Max Sum - Calculate sum excluding min/max",
    "pairofsongs60.py": "Pairs of Songs - Find pairs with total duration 60 seconds",
    "partitionlabels.py": "Partition Labels - Partition string with no repeated characters",
    "pattern.py": "Pattern - Implement pattern matching",
    "perfect_square.py": "Perfect Square - Check if number is perfect square",
    "person_class.py": "Person Class - Implement person class",
    "phone_number_permutations.py": "Phone Number Letter Combinations",
    "practice_apple.py": "Practice Apple - Practice problem solution",
    "problem.py": "Problem - Solve problem",
    "pythonlight.py": "Python Light - Python learning exercise",
    "quicksort.py": "Quick Sort - Sort using quick sort algorithm",
    "random_llist.py": "Random Node from Linked List - Return random node",
    "ransome_note.py": "Ransom Note - Check if ransom note constructible",
    "reach_number.py": "Reach Number - Find steps to reach target",
    "recursivefibonacci.py": "Fibonacci - Calculate fibonacci number recursively",
    "removeduplicates_i_i.py": "Remove Duplicates - Remove duplicate elements",
    "replace_elements.py": "Replace Elements - Replace with right greatest",
    "reverse_integer.py": "Reverse Integer - Reverse digits of integer",
    "reverse_linked_list.py": "Reverse Linked List - Reverse a linked list",
    "sametree.py": "Same Tree - Check if two trees are identical",
    "selectionsort.py": "Selection Sort - Sort using selection sort algorithm",
    "sell_stock.py": "Best Time to Buy Sell Stock - Maximum profit from stocks",
    "sentinel.py": "Sentinel - Sentinel pattern implementation",
    "single_number.py": "Single Number - Find single number in array",
    "song_selector.py": "Song Selector - Select songs based on criteria",
    "spiralmatrixtraversal.py": "Spiral Matrix Traversal - Traverse matrix in spiral order",
    "sqrt.py": "Square Root - Calculate integer square root",
    "squares_of_sorted_array.py": "Squares of Sorted Array - Return squares in order",
    "stringtonumber_atoi.py": "String to Number - Convert string to integer",
    "sub_array_checker.py": "Subarray Checker - Check for subarray with target sum",
    "swapping_zero_one.py": "Swapping Zeros and Ones - Swap zeros and ones",
    "task_scheduler.py": "Task Scheduler - Schedule tasks with minimum idle time",
    "throttling.py": "Throttling - Rate limiting implementation",
    "time_conversion.py": "Time Conversion - Convert time format",
    "turnstile.py": "Turnstile - Turnstile entry/exit tracking",
    "twosum.py": "Two Sum - Find two numbers that sum to target",
    "unique_linked_iist.py": "Unique Linked List - Remove duplicates",
    "utopiantree.py": "Utopian Tree - Track growth of utopian tree",
    "valid_parenthesis.py": "Valid Parentheses - Check if parentheses valid",
    "validpyramid.py": "Valid Pyramid - Check if array forms valid pyramid",
    "variants_count.py": "Variants Count - Count number of variants",
    "water_tank.py": "Water Tank - Calculate water trapped",
    "zigzag.py": "Zigzag - Zigzag pattern solution",
}


def camel_to_snake_case(name):
    """Convert camelCase to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def get_mapping_dict(content):
    """Extract camelCase to snake_case mappings from function definitions."""
    mappings = {}
    # Find all function definitions: def functionName(...):
    pattern = r'def\s+([a-zA-Z_]\w*)\s*\('
    for match in re.finditer(pattern, content):
        old_name = match.group(1)
        new_name = camel_to_snake_case(old_name)
        if old_name != new_name:
            mappings[old_name] = new_name
    return mappings


def add_module_docstring(content, filename):
    """Add module docstring if missing."""
    if content.strip().startswith('"""') or content.strip().startswith("'''"):
        return content

    problem_desc = PROBLEM_DESCRIPTIONS.get(filename, "Solution to LeetCode problem")
    docstring = f'"""{problem_desc}."""\n\n'
    return docstring + content


def rename_functions(content, mappings):
    """Rename all function definitions and calls."""
    for old_name, new_name in mappings.items():
        # Rename function definition
        pattern = rf'\bdef\s+{re.escape(old_name)}\s*\('
        content = re.sub(pattern, f'def {new_name}(', content)

        # Rename self.method calls
        pattern = rf'self\.{re.escape(old_name)}\s*\('
        content = re.sub(pattern, f'self.{new_name}(', content)

        # Rename function calls (standalone)
        pattern = rf'\b{re.escape(old_name)}\s*\('
        replacement = f'{new_name}('
        content = re.sub(pattern, replacement, content)

    return content


def add_docstrings(content):
    """Add basic docstrings to classes and functions."""
    lines = content.split('\n')
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]
        result.append(line)

        # Check if this is a class definition
        if re.match(r'^\s*class\s+\w+', line):
            indent = len(line) - len(line.lstrip())
            # Check if next line is docstring or not
            if i + 1 < len(lines) and '"""' not in lines[i + 1]:
                class_name = re.search(r'class\s+(\w+)', line).group(1)
                docstring = ' ' * (indent + 4) + f'"""{class_name} class."""'
                result.append(docstring)

        # Check if this is a function/method definition
        elif re.match(r'^\s*def\s+\w+', line):
            indent = len(line) - len(line.lstrip())
            # Check if next line is docstring or not
            if i + 1 < len(lines) and '"""' not in lines[i + 1] and "'''" not in lines[i + 1]:
                func_name = re.search(r'def\s+(\w+)', line).group(1)
                docstring = ' ' * (indent + 4) + f'"""{func_name} function."""'
                result.append(docstring)

        i += 1

    return '\n'.join(result)


def process_file(filepath, skip_already_refactored=True):
    """Process a single Python file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        filename = os.path.basename(filepath)

        # Skip already manually refactored files
        if skip_already_refactored and ("Args:" in content or "Returns:" in content):
            print(f"Skipped (already refactored): {filename}")
            return False

        original_content = content

        # 1. Add module docstring
        if not (content.strip().startswith('"""') or content.strip().startswith("'''")):
            content = add_module_docstring(content, filename)

        # 2. Get function name mappings
        mappings = get_mapping_dict(content)

        # 3. Rename functions if needed
        if mappings:
            content = rename_functions(content, mappings)

        # 4. Add basic docstrings (conservative approach)
        # Only add if file is simple enough
        if len(content.split('\n')) < 200 and 'Args:' not in content:
            content = add_docstrings(content)

        # Write back to file
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False


def main():
    """Main function to process all Python files."""
    repo_path = Path("/home/shivam/Github/pycode")
    python_files = sorted(repo_path.glob("*.py"))

    skip_files = {
        'refactor_script.py',
        'grader.py',
        'finalproject.py',
        'adding2_linked_lists.py',  # Already manually refactored
        'banking_l_d.py',  # Already manually refactored
        'Test.java',  # Not Python
    }

    processed = 0
    skipped = 0

    for py_file in python_files:
        if py_file.name in skip_files or not py_file.name.endswith('.py'):
            continue

        if process_file(py_file):
            processed += 1
            print(f"✓ Processed: {py_file.name}")
        else:
            skipped += 1

    print(f"\n{'='*60}")
    print(f"Total files processed: {processed}")
    print(f"Files skipped (already refactored): {skipped}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
