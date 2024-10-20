import cv2


def visualize_detections(model, video_path, output_path):
    """
    Визуализирует детекции на видео и сохраняет выходной файл.
    """
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Кодек для сохранения видео
    out = cv2.VideoWriter(output_path, fourcc, 30.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Прогоняем кадр через модель
        results = model.predict(frame)

        # Визуализация предсказаний на кадре
        annotated_frame = results[0].plot()
        out.write(annotated_frame)

    cap.release()
    out.release()
    print(f"Saved annotated video to {output_path}")
