import pygame

pygame.init()

# Membuat judul window
pygame.display.set_caption("Simulasi Cermin Cekung")

# Fungsi menggambar garis
def draw_dda_line(canvas, x1, y1, x2, y2, r, g, b):
    # hitung perubahan pada sumbu x dan y
    dx = x2 - x1
    dy = y2 - y1

    # Tentukan jumlah langkah
    panjang_garis = max(abs(dx), abs(dy))
    
    if panjang_garis != 0:
        # Hitung penambahan per langkah
        x_increment = dx / panjang_garis
        y_increment = dy / panjang_garis
    else:
        x_increment = y_increment = 0

    # Inisialisasi titik awal
    x, y = x1, y1

    # Inisialisasi warna
    warna = (r, g, b)

    # Gambar garis
    for _ in range(int(panjang_garis)):
        canvas.set_at((int(x), int(y)), warna)
        x += x_increment
        y += y_increment

# Fungsi menggambar lingkaran
def draw_dda_circle(canvas, x, y, radius, r, g, b):
    for i in range(int(x - radius), int(x + radius + 1)):
        for j in range(int(y - radius), int(y + radius + 1)):
            if (i - x) ** 2 + (j - y) ** 2 <= radius ** 2:
                canvas.set_at((i, j), (r, g, b))

# Membuat garis kartesius sumbu x
def gariskoor_x(x):
    return int(canvas.get_width() // 2 + x * (-1))

# Membuat garis kartesius sumbu y
def gariskoor_y(y):
    return int(canvas.get_height() // 2 + y * (-1))

# Menghitung jarak bayangan
def jarak_bayangan(s, f):
    s_aks =  (s * f) / (s - f)
    return s_aks

# Menghitung tinggi bayangan
def tinggi_bayangan(s, h, s_aks):
    h_aks = (s_aks / s) * h
    return h_aks

# Inisialisasi ukuran canvas
width, height = 1000, 500
canvas = pygame.display.set_mode((width, height))
white = (255, 255, 255)
canvas.fill(white)
red = (255,0,0)

# menggamber garis vertikal 
x1, y1 = int(width / 2) , 0
x2 , y2 = int(width / 2) , height
draw_dda_line(canvas, x1, y1, x2, y2, 0,0,0)

#menggambar garis horizontal 
x1, y1 = 0 , height / 2
x2, y2 = width, height / 2
draw_dda_line(canvas, x1, y1, x2, y2, 0,0,0)

# input sementara
jarak_benda = 301 
tinggi_benda = 52
titik_fokus = 153

jarakBayangan = int(jarak_bayangan(jarak_benda, titik_fokus))
tinggiBayangan = int(tinggi_bayangan(jarak_benda, tinggi_benda, jarakBayangan))
scale_factor = 1.0

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit( 0 )
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                jarak_benda -= 5
                print('Right arrow key pressed')
            if event.key == pygame.K_LEFT:
                jarak_benda += 5
                print('Left arrow key pressed')
            if event.key == pygame.K_DOWN:
                tinggi_benda -= 5
                scale_factor -= 0.1
                print('Down arrow key pressed')
            if event.key == pygame.K_UP:
                tinggi_benda += 5
                scale_factor += 0.1
                print('Up arrow key pressed')

    # Clear layar
    canvas.fill(white)
    
    # Gambar garis koordinat
    x1, y1 = int(width / 2), 0
    x2, y2 = int(width / 2), height
    draw_dda_line(canvas, x1, y1, x2, y2, 0, 0, 0)

    x1, y1 = 0, height / 2
    x2, y2 = width, height / 2
    draw_dda_line(canvas, x1, y1, x2, y2, 0, 0, 0)

    # Update positions and draw objects
    jarakBayangan = int(jarak_bayangan(jarak_benda, titik_fokus))
    tinggiBayangan = int(tinggi_bayangan(jarak_benda, tinggi_benda, jarakBayangan))
        
    # Menggambar titik fokus
    x1, y1 = gariskoor_x(titik_fokus), gariskoor_y(1)
    x2, y2 = gariskoor_x(titik_fokus), gariskoor_y(-1)
    pygame.draw.line(canvas, red, (x1,y1), (x2,y2), 5)

    # Benda
    lebar_body_mobil = 80  * scale_factor 
    tinggi_body_mobil = 40 * scale_factor 

    x1, y1 = gariskoor_x(jarak_benda - lebar_body_mobil/1.5), gariskoor_y(tinggi_benda - tinggi_body_mobil)
    x2, y2 = gariskoor_x(jarak_benda + lebar_body_mobil/1.5), gariskoor_y(tinggi_benda - tinggi_body_mobil)
    draw_dda_line(canvas, x1, y1, x2, y2, 255, 0, 0)  # garis A1

    x1, y1 = gariskoor_x(jarak_benda + lebar_body_mobil/1.5), gariskoor_y(tinggi_benda - tinggi_body_mobil)
    x2, y2 = gariskoor_x(jarak_benda + lebar_body_mobil/1.5), gariskoor_y(tinggi_benda - tinggi_body_mobil/2)
    draw_dda_line(canvas, x1, y1, x2, y2, 255, 0, 0)  # garis B1

    x1, y1 = gariskoor_x(jarak_benda - lebar_body_mobil/1.5), gariskoor_y(tinggi_benda - tinggi_body_mobil)
    x2, y2 = gariskoor_x(jarak_benda - lebar_body_mobil/1.5), gariskoor_y(tinggi_benda - tinggi_body_mobil/2)
    draw_dda_line(canvas, x1, y1, x2, y2, 255, 0, 0)  # garis B2

    x1, y1 = gariskoor_x(jarak_benda + lebar_body_mobil/1.5), gariskoor_y(tinggi_benda - tinggi_body_mobil/2)
    x2, y2 = gariskoor_x(jarak_benda + lebar_body_mobil/2.5), gariskoor_y(tinggi_benda - tinggi_body_mobil/2)
    draw_dda_line(canvas, x1, y1, x2, y2, 255, 0, 0)  # garis A2

    x1, y1 = gariskoor_x(jarak_benda - lebar_body_mobil/1.5), gariskoor_y(tinggi_benda - tinggi_body_mobil/2)
    x2, y2 = gariskoor_x(jarak_benda - lebar_body_mobil/2.5), gariskoor_y(tinggi_benda - tinggi_body_mobil/2)
    draw_dda_line(canvas, x1, y1, x2, y2, 255, 0, 0)  # garis A3

    x1, y1 = gariskoor_x(jarak_benda + lebar_body_mobil/2.5), gariskoor_y(tinggi_benda - tinggi_body_mobil/2)
    x2, y2 = gariskoor_x(jarak_benda + lebar_body_mobil/4), gariskoor_y(tinggi_benda)
    draw_dda_line(canvas, x1, y1, x2, y2, 255, 0, 0)  # garis C1

    x1, y1 = gariskoor_x(jarak_benda - lebar_body_mobil/2.5), gariskoor_y(tinggi_benda - tinggi_body_mobil/2)
    x2, y2 = gariskoor_x(jarak_benda - lebar_body_mobil/4), gariskoor_y(tinggi_benda)
    draw_dda_line(canvas, x1, y1, x2, y2, 255, 0, 0)  # garis C2

    x1, y1 = gariskoor_x(jarak_benda + lebar_body_mobil/4), gariskoor_y(tinggi_benda)
    x2, y2 = gariskoor_x(jarak_benda - lebar_body_mobil/4), gariskoor_y(tinggi_benda)
    draw_dda_line(canvas, x1, y1, x2, y2, 255, 0, 0)  # garis A4

    # Menggambar ban mobil
    wheel_radius = 12  * scale_factor # Jari-jari ban mobil

    x1, y1 = gariskoor_x(jarak_benda - lebar_body_mobil/5 - wheel_radius), gariskoor_y(tinggi_body_mobil/3.5)
    draw_dda_circle(canvas, x1, y1, wheel_radius, 255, 0, 0)  # Ban kiri

    x1, y1 = gariskoor_x(jarak_benda + lebar_body_mobil/5 + wheel_radius), gariskoor_y(tinggi_body_mobil/3.5)
    draw_dda_circle(canvas, x1, y1, wheel_radius, 255, 0, 0)  # Ban kanan

    # Bayangan
    lebar_bayangan_mobil = 80  * scale_factor # lebar badan mobil
    tinggi_bayangan_mobil = 40 * scale_factor # tinggi badan mobil

    x1, y1 = gariskoor_x(jarakBayangan - lebar_bayangan_mobil/1.5), gariskoor_y(-tinggiBayangan + tinggi_bayangan_mobil)
    x2, y2 = gariskoor_x(jarakBayangan + lebar_bayangan_mobil/1.5), gariskoor_y(-tinggiBayangan + tinggi_bayangan_mobil)
    draw_dda_line(canvas, x1, y1, x2, y2, 255, 0, 0)  # garis A1

    x1, y1 = gariskoor_x(jarakBayangan + lebar_bayangan_mobil/1.5), gariskoor_y(-tinggiBayangan + tinggi_bayangan_mobil)
    x2, y2 = gariskoor_x(jarakBayangan + lebar_bayangan_mobil/1.5), gariskoor_y(-tinggiBayangan + tinggi_bayangan_mobil/2)
    draw_dda_line(canvas, x1, y1, x2, y2, 255, 0, 0)  # garis B1

    x1, y1 = gariskoor_x(jarakBayangan - lebar_bayangan_mobil/1.5), gariskoor_y(-tinggiBayangan + tinggi_bayangan_mobil)
    x2, y2 = gariskoor_x(jarakBayangan - lebar_bayangan_mobil/1.5), gariskoor_y(-tinggiBayangan + tinggi_bayangan_mobil/2)
    draw_dda_line(canvas, x1, y1, x2, y2, 255, 0, 0)  # garis B2

    x1, y1 = gariskoor_x(jarakBayangan + lebar_bayangan_mobil/1.5), gariskoor_y(-tinggiBayangan + tinggi_bayangan_mobil/2)
    x2, y2 = gariskoor_x(jarakBayangan + lebar_bayangan_mobil/2.5), gariskoor_y(-tinggiBayangan + tinggi_bayangan_mobil/2)
    draw_dda_line(canvas, x1, y1, x2, y2, 255, 0, 0)  # garis A2

    x1, y1 = gariskoor_x(jarakBayangan - lebar_bayangan_mobil/1.5), gariskoor_y(-tinggiBayangan + tinggi_bayangan_mobil/2)
    x2, y2 = gariskoor_x(jarakBayangan - lebar_bayangan_mobil/2.5), gariskoor_y(-tinggiBayangan + tinggi_bayangan_mobil/2)
    draw_dda_line(canvas, x1, y1, x2, y2, 255, 0, 0)  # garis A3

    x1, y1 = gariskoor_x(jarakBayangan + lebar_bayangan_mobil/2.5), gariskoor_y(-tinggiBayangan + tinggi_bayangan_mobil/2)
    x2, y2 = gariskoor_x(jarakBayangan + lebar_bayangan_mobil/4), gariskoor_y(-tinggiBayangan)
    draw_dda_line(canvas, x1, y1, x2, y2, 255, 0, 0)  # garis C1

    x1, y1 = gariskoor_x(jarakBayangan - lebar_bayangan_mobil/2.5), gariskoor_y(-tinggiBayangan + tinggi_bayangan_mobil/2)
    x2, y2 = gariskoor_x(jarakBayangan - lebar_bayangan_mobil/4), gariskoor_y(-tinggiBayangan)
    draw_dda_line(canvas, x1, y1, x2, y2, 255, 0, 0)  # garis C2

    x1, y1 = gariskoor_x(jarakBayangan + lebar_bayangan_mobil/4), gariskoor_y(-tinggiBayangan)
    x2, y2 = gariskoor_x(jarakBayangan - lebar_bayangan_mobil/4), gariskoor_y(-tinggiBayangan)
    draw_dda_line(canvas, x1, y1, x2, y2, 255, 0, 0)  # garis A4

    # Menggambar bayangan ban mobil
    wheel_radius = 12  * scale_factor # Jari-jari ban mobil

    x1, y1 = gariskoor_x(jarakBayangan- lebar_bayangan_mobil/5 - wheel_radius), gariskoor_y(-tinggiBayangan + tinggi_bayangan_mobil)
    draw_dda_circle(canvas, x1, y1, wheel_radius, 255, 0, 0)  # Ban kiri

    x1, y1 = gariskoor_x(jarakBayangan + lebar_bayangan_mobil/5 + wheel_radius), gariskoor_y(-tinggiBayangan + tinggi_bayangan_mobil)
    draw_dda_circle(canvas, x1, y1, wheel_radius, 255, 0, 0)  # Ban kanan

    # Garis istimewa 1
    x1, y1 = gariskoor_x(jarak_benda), gariskoor_y(tinggi_benda)
    x2, y2 = int(width / 2), gariskoor_y(tinggi_benda)
    draw_dda_line(canvas, x1, y1, x2, y2, 66, 66, 245)

    x1, y1 = int(width / 2), gariskoor_y(tinggi_benda)
    x2, y2 = gariskoor_x(titik_fokus), gariskoor_y(0)
    draw_dda_line(canvas, x1, y1, x2, y2, 66, 66, 245)

    x1, y1 = gariskoor_x(titik_fokus), gariskoor_y(0)
    x2, y2 = gariskoor_x(jarakBayangan), gariskoor_y(-tinggiBayangan)
    draw_dda_line(canvas, x1, y1, x2, y2, 66, 66, 245)

    # Garis istimewa 2
    x1, y1 = gariskoor_x(jarak_benda), gariskoor_y(tinggi_benda)
    x2, y2 = gariskoor_x(titik_fokus), gariskoor_y(0)
    draw_dda_line(canvas, x1, y1, x2, y2, 1, 117, 24)

    x1, y1 = gariskoor_x(titik_fokus), gariskoor_y(0)
    x2, y2 = int(width/2), gariskoor_y(-tinggiBayangan)
    draw_dda_line(canvas, x1, y1, x2, y2, 1, 117, 24)

    x1, y1 = int(width/2), gariskoor_y(-tinggiBayangan)
    x2, y2 = gariskoor_x(jarakBayangan), gariskoor_y(-tinggiBayangan)
    draw_dda_line(canvas, x1, y1, x2, y2, 1, 117, 24)

        
    pygame.display.flip()