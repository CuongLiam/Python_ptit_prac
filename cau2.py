def tinh_tien_nuoc(m3, so_nguoi):


    GIA_BAC_1 = 9206
    GIA_BAC_2 = 17725
    GIA_BAC_3 = 19786

    limit_bac_1 = 4 * so_nguoi
    limit_bac_2 = 6 * so_nguoi

    tong_tien = 0

    if (m3 <= limit_bac_1):
        tong_tien = m3 * GIA_BAC_1

    elif (m3 <= limit_bac_2):
        tien_bac_1 = limit_bac_1 * GIA_BAC_1

        phan_con_lai = m3 - limit_bac_1
        tien_bac_2 = phan_con_lai * GIA_BAC_2

        tong_tien = tien_bac_1 + tien_bac_2

    else:
        tien_bac_1 = limit_bac_1 * GIA_BAC_1

        # Tính trọn bậc 2 (khoảng cách từ 4m3 đến 6m3 là 2m3/người)
        khoi_luong_bac_2 = limit_bac_2 - limit_bac_1  # hoặc 2 * so_nguoi
        tien_bac_2 = khoi_luong_bac_2 * GIA_BAC_2

        # Phần còn lại tính giá bậc 3
        phan_con_lai = m3 - limit_bac_2
        tien_bac_3 = phan_con_lai * GIA_BAC_3

        tong_tien = tien_bac_1 + tien_bac_2 + tien_bac_3
    return int(round(tong_tien))


# --- CHẠY THỬ (TEST CASE) THEO ĐỀ BÀI ---
print(f"tinh_tien_nuoc(4, 1)  -> {tinh_tien_nuoc(4, 1)}")   # Kỳ vọng: 36824
print(f"tinh_tien_nuoc(8, 2)  -> {tinh_tien_nuoc(8, 2)}")   # Kỳ vọng: 73648
print(f"tinh_tien_nuoc(10, 2) -> {tinh_tien_nuoc(10, 2)}")  # Kỳ vọng: 109098
print(f"tinh_tien_nuoc(20, 2) -> {tinh_tien_nuoc(20, 2)}")  # Kỳ vọng: 302836