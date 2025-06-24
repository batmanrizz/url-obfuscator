<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" height="64" alt="Google Logo"/>
</p>

# URL Generator Script

This is a simple Python script that generates a custom URL based on your inputted domain name and saves it to a file called `url.txt`.

---

## 🚀 Features

- Interactive prompt for your domain name  
- Formats a premade URL string with your input  
- Saves the result automatically to `url.txt`  
- No dependencies required—just Python!

---

## 📸 Preview

![example image](https://user-images.githubusercontent.com/25181517/212271095-7a2d2e7a-2db6-4eec-9b1d-7fa1d2ffb6e7.png)

---

## 🛠️ How to Use

1. **Clone this repo** (or just copy the code):

    ```bash
    git clone https://github.com/yourusername/url-generator.git
    cd url-generator
    ```

2. **Run the script:**

    ```bash
    python generate_url.py
    ```

3. **Follow the prompt:**

    ```
    Enter your domain name--> example.com
    ```

4. **Check the output:**  
   The URL will be saved in a file called `url.txt` in the same directory.

---

## 📝 Example

If you enter:

```
Enter your domain name--> example.com
```

The content of `url.txt` will be:

```
https://accounts.google.com+signin=secure+v2+identifier=passive@example.com
```

---

## 🧩 Script

```python
url_end = input("Enter your domain name--> ")

url = f"https://accounts.google.com+signin=secure+v2+identifier=passive@{url_end}"

with open("url.txt", "w") as f:
    f.write(url)
```

---

<p align="center">
  <img src="https://cdn.iconscout.com/icon/free/png-256/python-3521655-2945099.png" height="40" alt="Python Logo"/>
</p>

---
