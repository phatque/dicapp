import pandas as pd
import json
from tkinter import Tk, Label, Button, filedialog, messagebox

# Hàm để chọn file Excel và chuyển đổi sang JSON
def convert_excel_to_json():
    # Hiển thị hộp thoại chọn file Excel
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    
    if file_path:
        try:
            # Đọc file Excel
            excel_data = pd.read_excel(file_path)

            # Kiểm tra xem các cột có tồn tại không
            required_columns = ['Từ vựng', 'Nghĩa']
            optional_columns = ['Âm Hán', 'Từ vựng 2', 'Âm Hán 2', 'Nghĩa 2']

            for col in required_columns:
                if col not in excel_data.columns:
                    messagebox.showerror("Lỗi", f"File Excel không có cột bắt buộc '{col}'")
                    return

            # Lọc các cột bắt buộc
            filtered_data = excel_data[required_columns].copy()

            # Chỉ thêm các cột tùy chọn nếu chúng tồn tại
            for col in optional_columns:
                if col in excel_data.columns:
                    filtered_data[col] = excel_data[col]

            # Không sử dụng dropna() để đảm bảo mọi dòng, kể cả dòng có dữ liệu trống, đều được giữ lại
            # Chuyển đổi thành JSON, với các giá trị trống giữ nguyên (sẽ là null trong JSON)
            json_data = filtered_data.to_dict(orient='records')

            # Lưu file JSON
            json_file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
            if json_file_path:
                with open(json_file_path, 'w', encoding='utf-8') as json_file:
                    json.dump(json_data, json_file, ensure_ascii=False, indent=4)
                
                messagebox.showinfo("Thành công", f"Dữ liệu đã được chuyển đổi và lưu thành công vào {json_file_path}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

# Giao diện người dùng bằng Tkinter
def create_app():
    window = Tk()
    window.title("Chuyển đổi Excel sang JSON")
    
    # Tiêu đề
    label = Label(window, text="Chuyển đổi Excel sang JSON", font=("Arial", 14))
    label.pack(pady=20)

    # Nút "Chọn file Excel và Convert"
    convert_button = Button(window, text="Chọn file Excel và Convert", command=convert_excel_to_json, width=30, height=2)
    convert_button.pack(pady=20)

    # Chạy ứng dụng
    window.geometry("400x200")
    window.mainloop()

# Chạy ứng dụng
if __name__ == "__main__":
    create_app()
