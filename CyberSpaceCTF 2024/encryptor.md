- Given an APK package

![image](https://github.com/user-attachments/assets/b63f3e2e-203a-4db6-bad2-ffd05fb6baa2)

- Since this is my first time dealing with reversing APK, after some digging i was able to identify the main function (Main Activity) of the apk using jadx

![image](https://github.com/user-attachments/assets/e735e9bf-39e8-4c71-aca6-53926774e506)


```java
package com.example.encryptor;

import android.app.AlertDialog;
import android.content.Context;
import android.content.res.AssetManager;
import android.os.Build;
import android.os.Bundle;
import android.util.Base64;
import android.view.View;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.SecretKeySpec;

/* loaded from: classes.dex */
public class MainActivity extends AppCompatActivity {
    AlertDialog.Builder builder;

    /* JADX INFO: Access modifiers changed from: protected */
    @Override // androidx.fragment.app.FragmentActivity, androidx.activity.ComponentActivity, androidx.core.app.ComponentActivity, android.app.Activity
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView(R.layout.activity_main);
        this.builder = new AlertDialog.Builder(this);
    }

    private String getKey() {
        return new String(Base64.decode("ZW5jcnlwdG9yZW5jcnlwdG9y".getBytes(), 0));
    }

    private String encryptText(String str) throws InvalidKeyException, UnsupportedEncodingException, NoSuchPaddingException, NoSuchAlgorithmException, IllegalBlockSizeException, BadPaddingException {
        SecretKeySpec secretKeySpec = new SecretKeySpec(getKey().getBytes("UTF-8"), "Blowfish");
        Cipher cipher = Cipher.getInstance("Blowfish");
        if (cipher == null) {
            throw new Error();
        }
        cipher.init(1, secretKeySpec);
        return Build.VERSION.SDK_INT >= 26 ? new String(Base64.encode(cipher.doFinal(str.getBytes("UTF-8")), 0)) : "";
    }

    public void encrypt_onClick(View view) throws UnsupportedEncodingException, NoSuchPaddingException, IllegalBlockSizeException, NoSuchAlgorithmException, BadPaddingException, InvalidKeyException {
        this.builder.setMessage(encryptText(((TextView) findViewById(R.id.input)).getText().toString())).setCancelable(true);
        AlertDialog create = this.builder.create();
        create.setTitle("Here's your encrypted text:");
        create.show();
        View findViewById = create.findViewById(android.R.id.message);
        if (findViewById instanceof TextView) {
            ((TextView) findViewById).setTextIsSelectable(true);
        }
    }

    public static String readAssetFile(Context context, String str) {
        AssetManager assets = context.getAssets();
        StringBuilder sb = new StringBuilder();
        try {
            InputStream open = assets.open(str);
            try {
                BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(open));
                while (true) {
                    try {
                        String readLine = bufferedReader.readLine();
                        if (readLine == null) {
                            break;
                        }
                        sb.append(readLine).append('\n');
                    } finally {
                    }
                }
                bufferedReader.close();
                if (open != null) {
                    open.close();
                }
            } finally {
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return sb.toString();
    }

    public void getflag_onClick(View view) {
        this.builder.setMessage(readAssetFile(this, "enc.txt")).setCancelable(true);
        AlertDialog create = this.builder.create();
        create.setTitle("Here's the encrypted flag:");
        create.show();
        View findViewById = create.findViewById(android.R.id.message);
        if (findViewById instanceof TextView) {
            ((TextView) findViewById).setTextIsSelectable(true);
        }
    }
}
```

- The flow of this program is pretty straightfoward. First it decode the base64 encoded key to a stream of bytes then it encrypt the users' input using Blowfish algorithm with ECB mode
- With these pieces of information, writing a decrypting will be easy but without the encrypted flag we can't really do anything . But worry not, there is a file named `enc.txt` in `Resources/assets`

  ![image](https://github.com/user-attachments/assets/1048368e-0cb8-4bcc-92ed-6e2103fe95ee)
  ![image](https://github.com/user-attachments/assets/a1b26608-1004-4e32-9ade-eb04256d8c5f)

- Now is time to write the script

```python
from Crypto.Cipher import Blowfish
from base64 import *
bs = Blowfish.block_size
cyphertext = b64decode('OIkZTMehxXAvICdQSusoDP6Hn56nDiwfGxt7w/Oia4oxWJE3NVByYnOMbqTuhXKcgg50DmVpudg=')
key = b64decode('ZW5jcnlwdG9yZW5jcnlwdG9y')
cypher = Blowfish.new(key, Blowfish.MODE_ECB)
msg = cypher.decrypt(cyphertext)
last_byte = msg[-1]
msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]
print(msg)
```

![image](https://github.com/user-attachments/assets/86c035cb-35aa-4ea5-ac87-9c6c724618ff)

**Flag:** `CSCTF{3ncrypt0r_15nt_s4Fe_w1th_4n_h4Rdc0d3D_k3y!}`


