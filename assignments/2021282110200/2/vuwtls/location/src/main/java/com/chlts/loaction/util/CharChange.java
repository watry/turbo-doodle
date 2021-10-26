package com.chlts.loaction.util;

public class CharChange {
    public static String unicodeToCn(String unicode) {
        String[] strs = unicode.split("\\\\u");
        String returnStr = "";
        for (int i = 1; i < strs.length; i++) {
            returnStr += (char) Integer.valueOf(strs[i], 16).intValue();
        }
        return returnStr;
    }
}
