# GitHub: Who Doesn't Follow You Back?

This is a simple JavaScript script that can be executed directly in the **browser console** (preferably in Google Chrome) while you're logged into your **GitHub** account.

It allows you to quickly identify **who you follow that doesn’t follow you back**.

## How It Works

The script makes asynchronous requests to your GitHub pages for:

-   **Following** (`following`)    
-   **Followers** (`followers`)
    

It then compares both lists and displays the users you follow who **do not follow you back**.

## How to Use

1.  Go to GitHub and **log in** to your account: [https://github.com](https://github.com)    
2.  Press `F12` or right-click anywhere on the page and choose **“Inspect”** to open DevTools    
3.  Navigate to the **Console** tab    
4.  Paste the script and press **Enter**    
5.  ⚠️ If your browser blocks pasting, type `allow pasting` in the console before pasting the code    

## ⚠️ Important Notes

-   This script **does not use the official GitHub API** (which has rate limits), but instead scrapes data from the web interface    
-   Changes to GitHub's layout may **break the script** in the future    
-   For accounts with many followers/following, the process may take a few seconds to complete    
-   GitHub may temporarily limit or block access if excessive requests are detected — use responsibly    
-   **Users without a visible display name** will not be detected correctly and may be skipped in the results

## License

Distributed under the **MIT License**.  
Feel free to modify, use, and share — **no warranties provided**.