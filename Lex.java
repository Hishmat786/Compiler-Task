import java.util.Scanner;

public class Lex{

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a Java code snippet: ");
        String code = scanner.nextLine();

    //define keywords here
    String[] keywords = {
            "abstract", "assert", "boolean", "break", "byte",
            "case", "catch", "char", "class", "const",
            "continue", "default", "do", "double", "else",
            "enum", "extends", "final", "finally", "float",
            "for", "goto", "if", "implements", "import",
            "instanceof", "int", "interface", "long", "native",
            "new", "package", "private", "protected", "public",
            "return", "short", "static", "strictfp", "super",
            "switch", "synchronized", "this", "throw", "throws",
            "transient", "try", "void", "volatile", "while"
        };

        String[] operators= {"+","-","*","/"};
        String[] punctuations= {";",":",",","','"};

    for (String keyword : keywords) {
            if (code.contains(keyword)) {
                System.out.println("Keyword '" + keyword + "' found.");        
            }    
    }
    for (String operator : operators) {
        if (code.contains(operator)) {
            System.out.println("Operator '" + operator + "' found.");        
        }    
    }
    for (String punctuation : punctuations) {
        if (code.contains(punctuation)) {
            System.out.println("Punctuation '" + punctuation + "' found.");        
        }    
    }

    }
}