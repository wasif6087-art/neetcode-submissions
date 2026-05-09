class Solution {

    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length()) return false;

        HashMap <Character, Integer> countS = new HashMap<>();
        HashMap <Character, Integer> countT = new HashMap<>();

        for (int i = 0; i<s.length(); i++) {
            char cs = s.charAt(i);
            char ct = t.charAt(i);

            countS.put(cs, countS.getOrDefault(cs,0)+1);

            countT.put(ct,countT.getOrDefault(ct,0) + 1);
        }

        return countS.equals(countT);




    }
}