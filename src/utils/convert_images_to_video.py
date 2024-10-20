import os
from moviepy.editor import ImageSequenceClip

# import cv2
#
#
# def images_to_video(image_folder, output_video, fps=30):
#     """
#     Создает видео из изображений в указанной папке.
#
#     :param image_folder: Путь к папке с изображениями.
#     :param output_video: Имя выходного видеофайла.
#     :param fps: Количество кадров в секунду (frames per second) для видео.
#     """
#
#     images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
#
#     if len(images) == 0:
#         raise ValueError("В указанной папке нет изображений!")
#     images.sort()
#     temp = cv2.imread(f"{image_folder}/{images[0]}", 1)
#     temp = cv2.cvtColor(temp, cv2.COLOR_RGB2GRAY)
#     frame = temp
#     height, width = frame.shape
#
#     video = cv2.VideoWriter(output_video, 0, 1, (width, height))
#
#     for image in images:
#         im = cv2.imread(os.path.join(image_folder, image))
#         im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
#
#         video.write(im)
#
#     cv2.destroyAllWindows()
#     video.release()
#     print(f"Видео сохранено как {output_video}")
#
#

def images_to_video(path, output_video):

    # Получите список всех изображений в папке
    images = [os.path.join(path, img) for img in os.listdir(path) if img.endswith(".jpg")]
    images.sort()  # Отсортируйте изображения по порядку

    # Частота кадров (FPS)
    fps = 24

    # Создайте видеоклип из последовательности изображений
    clip = ImageSequenceClip(images, fps=fps)

    # Сохраните видео в формате mp4
    clip.write_videofile(f"{output_video}.mp4", codec="libx264")