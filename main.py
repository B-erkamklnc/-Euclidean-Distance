from distance_calculator import DistanceCalculator
import matplotlib.pyplot as plt


class DistanceVisualizer:
    @staticmethod
    def plot_min_distance(points, min_pair, min_distance):
        """
        Minimum mesafeyi ve noktaları grafik üzerinde görselleştirir.
        points: Tüm noktalar [(x1, y1), (x2, y2), ...]
        min_pair: Minimum mesafeye sahip nokta çifti
        min_distance: Minimum mesafe
        """
        x_values = [min_pair[0][0], min_pair[1][0]]
        y_values = [min_pair[0][1], min_pair[1][1]]

        x_coords, y_coords = zip(*points)
        plt.scatter(x_coords, y_coords, label="Noktalar", color="blue")
        plt.plot(x_values, y_values, color='red', label=f'Minimum Mesafe: {min_distance:.2f}')
        
        plt.title("Koordinatlar ve En Kısa Mesafe")
        plt.xlabel("X Eksen")
        plt.ylabel("Y Eksen")
        plt.legend()
        plt.grid(True)
        plt.show()


def main():
    while True:
        piece = DistanceCalculator.input_control("integer", "Kaç noktanız var? ")
        points = []
        for i in range(piece):
            line_segment = tuple(
                DistanceCalculator.input_control("float", f"{i + 1}. noktanın (x{i + 1}, y{i + 1}) koordinatlarını giriniz: ")
            )
            points.append(line_segment)
        print(f"Noktaların koordinatları: {points}")

        while True:
            control = input("Noktaların koordinatlarını doğru ise 'y', yanlış ise 'n' tuşuna basınız: ")
            if control in ['y', 'n']:
                break
            else:
                print("Lütfen sadece 'y' veya 'n' tuşuna basınız.")

        if control == 'y':
            break

    # Mesafeleri hesapla
    distances = DistanceCalculator.euclidean_distance(points)

    # En düşük mesafeyi bul
    min_pair, min_distance = DistanceCalculator.find_min_distance(distances)
    print(f"En düşük öklit uzaklığının koordinatları: {min_pair[0]},{min_pair[1]} \nMesafesi: {min_distance}")

    # Grafiği çiz
    DistanceVisualizer.plot_min_distance(points, min_pair, min_distance)


if __name__ == "__main__":
    main()
