import time
import math
def nhap_bai_tap():
    # Nhập tên bài tập và độ khó
    ten_bai_tap = input("Nhập tên bài tập: ")
    do_kho = input("Nhập độ khó (Low, Medium, High): ").lower()
    
    return ten_bai_tap, do_kho

def tinh_thoi_gian_duoc_cho(do_kho):
    # Xác định thời gian cho bài tập dựa trên độ khó
    if do_kho == "low":
        return 10 * 60  # 10 phút
    elif do_kho == "medium":
        return 30 * 60  # 30 phút
    elif do_kho == "high":
        return 60 * 60  # 60 phút
    else:
        print("Độ khó không hợp lệ!")
        return None

def nhan_bai_tap(ten_bai_tap, do_kho):
    # Ghi nhận thời gian bắt đầu
    start_time = time.time()
    print(f"Đang làm bài {ten_bai_tap}... Độ khó: {do_kho.capitalize()}")
    
    # Đợi người dùng nhập khi hoàn thành bài tập
    input("Nhấn Enter khi đã hoàn thành bài tập...")
    
    # Ghi nhận thời gian kết thúc
    end_time = time.time()
    
    # Tính thời gian thực tế hoàn thành bài
    thoi_gian_hoan_thanh = end_time - start_time
    
    # Tính thời gian cho phép dựa trên độ khó
    thoi_gian_duoc_cho = tinh_thoi_gian_duoc_cho(do_kho)
    
    if thoi_gian_duoc_cho is None:
        return
    
    print(f"Thời gian hoàn thành: {thoi_gian_hoan_thanh:.2f} giây.")
    print(f"Thời gian yêu cầu cho bài tập này: {thoi_gian_duoc_cho} giây.")
    
    # Đánh giá mức độ hoàn thành
    if thoi_gian_hoan_thanh < thoi_gian_duoc_cho - 200:
        print("Rất tốt! Bạn hoàn thành sớm hơn " + str(math.floor(thoi_gian_duoc_cho - thoi_gian_hoan_thanh)) + " giây so với yêu cầu.")
    elif thoi_gian_hoan_thanh >= thoi_gian_duoc_cho - 200 and thoi_gian_hoan_thanh <= thoi_gian_duoc_cho:
        print("Gần! Bạn hoàn thành gần đúng thời gian yêu cầu.")
    else:
        print("Trễ! Bạn hoàn thành quá thời gian yêu cầu.")
    
# Chạy chương trình
def main():
    ten_bai_tap, do_kho = nhap_bai_tap()
    nhan_bai_tap(ten_bai_tap, do_kho)

if __name__ == "__main__":
    main()
