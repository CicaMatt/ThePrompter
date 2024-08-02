import tiktoken

# Il codice fornito
code = """
import java.io.UnsupportedEncodingException;
import java.security.InvalidKeyException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.spec.KeySpec;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.SecretKeySpec;
import javax.crypto.spec.IvParameterSpec;
import java.util.Base64;
import java.util.Arrays;

public class TripleDESTest {

    private static final String ALGORITHM = "DESede";
    private static final String TRANSFORMATION = "DESede/CBC/PKCS5Padding";
    private static final String CHARSET = "UTF-8";
    private static final String SECRET_KEY = "HG58YZ3CR9";

    public static void main(String[] args) {
        try {
            TripleDESTest test = new TripleDESTest();
            String text = "kyle boon";

            // Encrypt
            String encryptedText = test.encrypt(text);
            System.out.println("Encrypted Text: " + encryptedText);

            // Decrypt
            String decryptedText = test.decrypt(encryptedText);
            System.out.println("Decrypted Text: " + decryptedText);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public String encrypt(String message) throws Exception {
        byte[] keyBytes = getKeyBytes();
        SecretKey key = new SecretKeySpec(keyBytes, ALGORITHM);
        Cipher cipher = Cipher.getInstance(TRANSFORMATION);

        // Generate a random IV
        byte[] iv = new byte[8];
        new java.security.SecureRandom().nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        cipher.init(Cipher.ENCRYPT_MODE, key, ivSpec);
        byte[] plainTextBytes = message.getBytes(CHARSET);
        byte[] cipherTextBytes = cipher.doFinal(plainTextBytes);

        // Encode the IV and ciphertext into Base64
        byte[] ivAndCipherText = new byte[iv.length + cipherTextBytes.length];
        System.arraycopy(iv, 0, ivAndCipherText, 0, iv.length);
        System.arraycopy(cipherTextBytes, 0, ivAndCipherText, iv.length, cipherTextBytes.length);

        return Base64.getEncoder().encodeToString(ivAndCipherText);
    }

    public String decrypt(String encryptedMessage) throws Exception {
        byte[] keyBytes = getKeyBytes();
        SecretKey key = new SecretKeySpec(keyBytes, ALGORITHM);
        Cipher cipher = Cipher.getInstance(TRANSFORMATION);

        // Decode Base64
        byte[] ivAndCipherText = Base64.getDecoder().decode(encryptedMessage);

        // Extract IV and ciphertext
        byte[] iv = Arrays.copyOfRange(ivAndCipherText, 0, 8);
        byte[] cipherTextBytes = Arrays.copyOfRange(ivAndCipherText, 8, ivAndCipherText.length);

        IvParameterSpec ivSpec = new IvParameterSpec(iv);
        cipher.init(Cipher.DECRYPT_MODE, key, ivSpec);
        byte[] plainTextBytes = cipher.doFinal(cipherTextBytes);

        return new String(plainTextBytes, CHARSET);
    }

    private byte[] getKeyBytes() throws NoSuchAlgorithmException, UnsupportedEncodingException {
        // Generate a 24-byte key from a 16-byte MD5 hash
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] digestOfPassword = md.digest(SECRET_KEY.getBytes(CHARSET));
        byte[] keyBytes = Arrays.copyOf(digestOfPassword, 24);
        for (int j = 0, k = 16; j < 8;) {
            keyBytes[k++] = keyBytes[j++];
        }
        return keyBytes;
    }
}
"""

# Conta i token
encoding = tiktoken.encoding_for_model("gpt-4o")
tokens = encoding.encode(code)
num_tokens = len(tokens)

print(f"Numero di token: {num_tokens}")
