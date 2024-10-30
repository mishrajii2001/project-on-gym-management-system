import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector

class GymManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GYM ERA")
        self.root.geometry("800x600")
        self.root.configure(bg="#212529")  # Dark background color for contrast

        # Logo Image
        logo_path = "C:/Users/VICKY MISHRA/Documents/code python/logo.png"
        try:
            logo_img = Image.open(logo_path)
            logo_img = logo_img.resize((150, 150), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_img)
            logo_label = tk.Label(self.root, image=self.logo_photo, bg="#212529")
            logo_label.pack(pady=10)
        except Exception as e:
            messagebox.showerror("Error", f"Logo image could not be loaded: {e}")

        # Title
        title_label = tk.Label(
            self.root,
            text="Welcome to MISHRA'S GYM",
            font=("Helvetica", 20, "bold"),
            bg="#212529",
            fg="#ff5733"  # Bright color for title text
        )
        title_label.pack(pady=10)

        # Member Management Frame with style
        member_frame = ttk.LabelFrame(self.root, text="Member Management", padding=(20, 10))
        member_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Apply custom style for labels and entries
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12), background="#212529", foreground="white")
        style.configure("TEntry", font=("Helvetica", 10))

        # Button styles
        style.configure("AddButton.TButton", font=("Helvetica", 10, "bold"), background="#28a745", foreground="white")  # Green button
        style.map("AddButton.TButton", background=[("active", "#5cb85c")])  # Lighter green on hover

        style.configure("ViewButton.TButton", font=("Helvetica", 10, "bold"), background="#007bff", foreground="white")  # Blue button
        style.map("ViewButton.TButton", background=[("active", "#5bc0de")])  # Lighter blue on hover

        # Entry Fields
        ttk.Label(member_frame, text="MemberID:").grid(row=0, column=0, padx=10, pady=5)
        self.member_id_entry = ttk.Entry(member_frame, width=25)
        self.member_id_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(member_frame, text="First Name:").grid(row=1, column=0, padx=10, pady=5)
        self.first_name_entry = ttk.Entry(member_frame, width=25)
        self.first_name_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(member_frame, text="Last Name:").grid(row=2, column=0, padx=10, pady=5)
        self.last_name_entry = ttk.Entry(member_frame, width=25)
        self.last_name_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(member_frame, text="Date of Birth (YYYY-MM-DD):").grid(row=3, column=0, padx=10, pady=5)
        self.dob_entry = ttk.Entry(member_frame, width=25)
        self.dob_entry.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(member_frame, text="Join Date (YYYY-MM-DD):").grid(row=4, column=0, padx=10, pady=5)
        self.join_date_entry = ttk.Entry(member_frame, width=25)
        self.join_date_entry.grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(member_frame, text="Membership Type:").grid(row=5, column=0, padx=10, pady=5)
        self.membership_id_entry = ttk.Entry(member_frame, width=25)
        self.membership_id_entry.grid(row=5, column=1, padx=10, pady=5)

        ttk.Label(member_frame, text="Phone Number:").grid(row=6, column=0, padx=10, pady=5)
        self.phone_entry = ttk.Entry(member_frame, width=25)
        self.phone_entry.grid(row=6, column=1, padx=10, pady=5)

        ttk.Label(member_frame, text="Email:").grid(row=7, column=0, padx=10, pady=5)
        self.email_entry = ttk.Entry(member_frame, width=25)
        self.email_entry.grid(row=7, column=1, padx=10, pady=5)

        # Buttons with custom styles
        add_member_button = ttk.Button(member_frame, text="Add Member", command=self.add_member, style="AddButton.TButton")
        add_member_button.grid(row=8, column=0, columnspan=2, pady=20)

    def add_member(self):
        member_id = self.member_id_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        dob = self.dob_entry.get()
        join_date = self.join_date_entry.get()
        membership_id = self.membership_id_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        # Insert member into the database
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='847239',
                database='GymManagement'
            )
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO Members (MemberID, FirstName, LastName, DOB, JoinDate, MembershipID, PhoneNumber, Email) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (member_id, first_name, last_name, dob, join_date, membership_id, phone, email)
            )
            connection.commit()
            messagebox.showinfo("Success", "Member added successfully!")
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def view_members(self):
        messagebox.showinfo("Info", "Display members functionality not implemented yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GymManagementApp(root)
    root.mainloop()
