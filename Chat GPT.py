import openai
import tkinter as tk

openai.api_key = "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"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,
        max_tokens =1024,
        n=1,
        stop=None,
        temperature = 0.8,
        )
    
    message = completions.choices[0].text
    return message

#GUI Interface
def display_response():
    input_text = input_field.get()
    response = generate_response(input_text)
    output_field.config(state = 'normal')
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, response)
    output_field.config(state = 'disabled')

root = tk.Tk()
root.title("♡ Eishu's Chat Bot ♡")
root.geometry("600x500")
root.configure(bg='pink')



input_field = tk.Entry(root, font=("Arial",12))
input_field.pack(pady=5)

submit_button = tk.Button(root, text ="Submit", bg = 'red', font=("Arial", 12), command =display_response)
submit_button.pack(pady=5)

output_field = tk.Text(root, font=("Arial", 12), bg='#8F8FBC', state='disabled')
output_field.pack(pady=5)

root.mainloop()
