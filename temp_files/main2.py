import movis as mv


def create_video(message: str):
    """
    :param message: текст бегущей строки
    :return: mp4 видео
    """

    scene_size = (1920, 1080)
    text_layer = mv.layer.Text(message, font_size=256, font_family='Helvetica', color='#ffffff')
    # duration = (text_layer.get_size()[0] // scene_size[0] + 1) * 5

    scene = mv.layer.Composition(size=scene_size, duration=5)
    scene.add_layer(mv.layer.Rectangle(scene.size, color='#fb4562'))  # Set background

    start_pos = scene.size[0] + text_layer.get_size()[0] // 2, scene.size[1] // 2

    scene.add_layer(
        text_layer,
        name='text',  # The layer item can be accessed by name
        # offset=0,  # Show the text after one second
        position=start_pos,  # The layer is centered by default, but it can also be specified explicitly
        anchor_point=(0.0, 0.0),
        opacity=1.0, scale=1.0, rotation=0.0,  # anchor point, opacity, scale, and rotation are also supported
        blending_mode='normal')  # Blending mode can be specified for each layer.
    end_pos = - text_layer.get_size()[0] // 2, scene.size[1] // 2
    scene['text'].position.enable_motion().extend(
        keyframes=[0.0, 5.0], values=[start_pos, end_pos], easings=['ease_in_out'])

    scene.write_video('output.mp4')


def convert_to_h264(file):
    """

    :param file: файл для конвертации
    :return: видео с кодеком H264
    """
    intro = mv.layer.Video(file)
    scene = mv.layer.Composition(size=(1920, 1080), duration=0.1)
    result = mv.concatenate([intro, scene])
    result.write_video(file)


def main():
    message = input('Введите текст бегущей строки: ')
    create_video(message)
    # convert_to_h264()


if __name__ == '__main__':
    main()

