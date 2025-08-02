import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

class BMIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("500x700")  # Increased height for footer
        self.root.resizable(False, False)
        
        # Create menu
        self.create_menu()
        
        # Variables
        self.height_unit = tk.StringVar(value="cm")
        self.weight_unit = tk.StringVar(value="kg")
        self.bmi_value = tk.StringVar()
        self.category = tk.StringVar()
        self.ideal_weight = tk.StringVar()
        self.diet_plan = tk.StringVar()
        self.exercise_plan = tk.StringVar()
        
        # Create UI
        self.create_widgets()
        
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
    
    def show_about(self):
        about_text = (
            "BMI Calculator\n\n"
            "Version: 1.0\n"
            "Developed by: Sheikh Md. Mahtabur Rahman\n\n"
            "Contact Information:\n"
            "Website: github.com/genomicinvader\n"
            "Mobile: +8801711434897\n\n"
            "© 2025 All Rights Reserved"
        )
        messagebox.showinfo("About BMI Calculator", about_text)
        
    def create_widgets(self):
        # Main container frame
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Styling
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        style.configure("Header.TLabel", font=("Arial", 14, "bold"))
        style.configure("Result.TLabel", font=("Arial", 12, "bold"))
        style.configure("Footer.TLabel", font=("Arial", 8))
        style.configure("Link.TLabel", font=("Arial", 8), foreground="blue")
        
        # Content frame
        content_frame = ttk.Frame(main_container)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        ttk.Label(content_frame, text="BMI Calculator", style="Header.TLabel").grid(row=0, column=0, columnspan=4, pady=10)
        
        # Height Section
        ttk.Label(content_frame, text="Height:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.height_entry = ttk.Entry(content_frame, width=10)
        self.height_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        ttk.Radiobutton(content_frame, text="cm", variable=self.height_unit, value="cm").grid(row=1, column=2, padx=5)
        ttk.Radiobutton(content_frame, text="inches", variable=self.height_unit, value="inches").grid(row=1, column=3, padx=5)
        
        # Weight Section
        ttk.Label(content_frame, text="Weight:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.weight_entry = ttk.Entry(content_frame, width=10)
        self.weight_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        
        ttk.Radiobutton(content_frame, text="kg", variable=self.weight_unit, value="kg").grid(row=2, column=2, padx=5)
        ttk.Radiobutton(content_frame, text="lbs", variable=self.weight_unit, value="lbs").grid(row=2, column=3, padx=5)
        
        # Calculate Button
        ttk.Button(content_frame, text="Calculate BMI", command=self.calculate_bmi).grid(
            row=3, column=0, columnspan=4, pady=20, sticky=tk.EW)
        
        # Results Frame
        results_frame = ttk.LabelFrame(content_frame, text="Results", padding=10)
        results_frame.grid(row=4, column=0, columnspan=4, sticky=tk.EW, pady=10)
        
        # BMI Result
        ttk.Label(results_frame, text="Your BMI:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Label(results_frame, textvariable=self.bmi_value, style="Result.TLabel").grid(row=0, column=1, sticky=tk.W, pady=5)
        
        # Category
        ttk.Label(results_frame, text="Category:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Label(results_frame, textvariable=self.category, style="Result.TLabel").grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Ideal Weight
        ttk.Label(results_frame, text="Ideal Weight:").grid(row=2, column=0, sticky=tk.W, pady=5)
        ttk.Label(results_frame, textvariable=self.ideal_weight, style="Result.TLabel").grid(row=2, column=1, sticky=tk.W, pady=5)
        
        # Recommendations Frame
        rec_frame = ttk.LabelFrame(content_frame, text="Recommendations", padding=10)
        rec_frame.grid(row=5, column=0, columnspan=4, sticky=tk.EW, pady=10)
        
        # Diet Plan
        ttk.Label(rec_frame, text="Diet Plan:").grid(row=0, column=0, sticky=tk.W, pady=5)
        diet_text = tk.Text(rec_frame, height=5, width=50, wrap=tk.WORD)
        diet_text.grid(row=1, column=0, sticky=tk.W, pady=5)
        diet_text.insert(tk.END, "Diet recommendations will appear here")
        diet_text.config(state=tk.DISABLED)
        self.diet_text = diet_text
        
        # Exercise Plan
        ttk.Label(rec_frame, text="Exercise Plan:").grid(row=2, column=0, sticky=tk.W, pady=5)
        exercise_text = tk.Text(rec_frame, height=5, width=50, wrap=tk.WORD)
        exercise_text.grid(row=3, column=0, sticky=tk.W, pady=5)
        exercise_text.insert(tk.END, "Exercise recommendations will appear here")
        exercise_text.config(state=tk.DISABLED)
        self.exercise_text = exercise_text
        
        # Clear Button
        ttk.Button(content_frame, text="Clear All", command=self.clear_fields).grid(
            row=6, column=0, columnspan=4, pady=20, sticky=tk.EW)
        
        # Configure grid weights
        content_frame.grid_rowconfigure(5, weight=1)  # Allow recommendations to expand
        for i in range(4):
            content_frame.grid_columnconfigure(i, weight=1)
        
        # Creator Information Footer
        footer_frame = ttk.Frame(main_container)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(0, 10))
        
        ttk.Label(footer_frame, text="Designed and developed by Sheikh Md. Mahtabur Rahman", 
                 style="Footer.TLabel").pack(side=tk.LEFT, padx=5)
        
        # Clickable GitHub link
        github_link = ttk.Label(footer_frame, text="github.com/genomicinvader", 
                               style="Link.TLabel", cursor="hand2")
        github_link.pack(side=tk.LEFT, padx=5)
        github_link.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/genomicinvader"))
        
        ttk.Label(footer_frame, text="Mobile: +8801711434897", 
                 style="Footer.TLabel").pack(side=tk.LEFT, padx=5)
    
    def calculate_bmi(self):
        try:
            # Get and validate inputs
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            
            if height <= 0 or weight <= 0:
                raise ValueError("Values must be positive")
            
            # Convert to metric units
            if self.height_unit.get() == "inches":
                height_m = height * 0.0254
            else:
                height_m = height / 100  # cm to meters
                
            if self.weight_unit.get() == "lbs":
                weight_kg = weight * 0.453592
            else:
                weight_kg = weight
                
            # Calculate BMI
            bmi = weight_kg / (height_m ** 2)
            self.bmi_value.set(f"{bmi:.1f}")
            
            # Determine category
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 25:
                category = "Normal weight"
            elif 25 <= bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"
            self.category.set(category)
            
            # Calculate ideal weight
            ideal_weight_kg = 22 * (height_m ** 2)  # 22 is considered ideal BMI
            if self.weight_unit.get() == "lbs":
                ideal_weight = ideal_weight_kg * 2.20462
                self.ideal_weight.set(f"{ideal_weight:.1f} lbs")
            else:
                self.ideal_weight.set(f"{ideal_weight_kg:.1f} kg")
            
            # Generate recommendations
            self.generate_recommendations(category, bmi)
            
        except ValueError as e:
            messagebox.showerror("Input Error", "Please enter valid positive numbers")
    
    def generate_recommendations(self, category, bmi):
        diet_plan = ""
        exercise_plan = ""
        
        if category == "Underweight":
            diet_plan = (
                "• Increase calorie intake with nutrient-dense foods\n"
                "• Eat 5-6 smaller meals throughout the day\n"
                "• Include healthy fats (avocados, nuts, olive oil)\n"
                "• Consume protein-rich foods (eggs, chicken, fish)\n"
                "• Add healthy carbs (whole grains, sweet potatoes)"
            )
            exercise_plan = (
                "• Strength training 3-4 times/week (focus on major muscle groups)\n"
                "• Moderate cardio 2-3 times/week (20-30 mins)\n"
                "• Include compound exercises (squats, deadlifts, bench press)\n"
                "• Avoid excessive cardio that burns too many calories"
            )
        
        elif category == "Normal weight":
            diet_plan = (
                "• Maintain balanced diet with all food groups\n"
                "• Focus on whole foods: fruits, vegetables, lean proteins\n"
                "• Limit processed foods and added sugars\n"
                "• Stay hydrated with 2-3 liters of water daily\n"
                "• Control portion sizes to maintain current weight"
            )
            exercise_plan = (
                "• 150 mins moderate aerobic activity weekly\n"
                "• Strength training 2 times/week (all major muscle groups)\n"
                "• Include flexibility exercises (yoga, stretching)\n"
                "• Stay active throughout the day (walking, taking stairs)"
            )
        
        elif category == "Overweight":
            diet_plan = (
                "• Create calorie deficit of 500 kcal/day\n"
                "• Focus on lean proteins and high-fiber foods\n"
                "• Reduce refined carbs and added sugars\n"
                "• Increase vegetable intake (half your plate)\n"
                "• Practice mindful eating and control portions"
            )
            exercise_plan = (
                "• 150-300 mins moderate cardio weekly (brisk walking, cycling)\n"
                "• Strength training 2-3 times/week\n"
                "• Include HIIT workouts 1-2 times/week\n"
                "• Increase daily activity (aim for 10,000 steps)"
            )
        
        else:  # Obese
            diet_plan = (
                "• Consult doctor or nutritionist for personalized plan\n"
                "• Aim for 1-2 lbs weight loss per week\n"
                "• Focus on high-volume, low-calorie foods (vegetables)\n"
                "• Reduce processed foods and sugary beverages\n"
                "• Track food intake and maintain food diary"
            )
            exercise_plan = (
                "• Start with low-impact activities (swimming, elliptical)\n"
                "• Gradually increase to 200-300 mins exercise/week\n"
                "• Include strength training 3 times/week\n"
                "• Consider supervised exercise program\n"
                "• Break activity into smaller sessions (3×10 mins)\n\n"
                "For personalized plans, contact: github.com/genomicinvader"
            )
        
        # Update recommendation text boxes
        self.diet_text.config(state=tk.NORMAL)
        self.diet_text.delete(1.0, tk.END)
        self.diet_text.insert(tk.END, diet_plan)
        self.diet_text.config(state=tk.DISABLED)
        
        self.exercise_text.config(state=tk.NORMAL)
        self.exercise_text.delete(1.0, tk.END)
        self.exercise_text.insert(tk.END, exercise_plan)
        self.exercise_text.config(state=tk.DISABLED)
    
    def clear_fields(self):
        self.height_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.height_unit.set("cm")
        self.weight_unit.set("kg")
        self.bmi_value.set("")
        self.category.set("")
        self.ideal_weight.set("")
        
        self.diet_text.config(state=tk.NORMAL)
        self.diet_text.delete(1.0, tk.END)
        self.diet_text.insert(tk.END, "Diet recommendations will appear here")
        self.diet_text.config(state=tk.DISABLED)
        
        self.exercise_text.config(state=tk.NORMAL)
        self.exercise_text.delete(1.0, tk.END)
        self.exercise_text.insert(tk.END, "Exercise recommendations will appear here")
        self.exercise_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()