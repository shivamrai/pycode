public List<Integer> findActiveBusinesses(List<Event> events) {
    
    
    ListIterator<String> listIterator = events.listIterator(occurances);
 
    while(listIterator.hasNext()) {
        //System.out.println(listIterator.next());
        occurances = listIterator.next() + occurances;
        }

}