
class DistanceCalculator:
    @staticmethod
    def input_control(data_type, message):
        """
        Kullanıcı girişini kontrol eder ve uygun türde bir değer döner.
        data_type: "float" veya "integer"
        message: Kullanıcıya gösterilecek mesaj.
        """
        while True:
            try:
                if data_type == "float":
                    series = input(message).split()
                    control = [float(series[i]) for i in range(2)]
                    return control
                elif data_type == "integer":
                    control = int(input(message))
                    if control > 1:
                        return control
                    else:
                        print("\nLütfen 1'den büyük bir değer giriniz!\n")
            except ValueError:
                print("\nLütfen tekrar deneyiniz!\n")

    @staticmethod
    def euclidean_distance(points):
        """
        Verilen noktalar arasındaki tüm Öklit mesafelerini hesaplar.
        points: Noktalar listesi [(x1, y1), (x2, y2), ...]
        """
        distances = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                distance = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 3)
                distances.append(((points[i], points[j]), distance))
        return distances

    @staticmethod
    def find_min_distance(distances):
        """
        En düşük mesafeyi ve buna ait noktaları bulur.
        distances: Mesafeler [(noktalar çifti, mesafe), ...]
        """
        return min(distances, key=lambda x: x[1])
