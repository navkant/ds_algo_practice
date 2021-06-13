import json
import os

import cv2

import db_config


def make_video(video_object):
    connection = db_config.get_connection()

    with connection.cursor() as cursor:
        sql = """
                SELECT
                    *
                FROM
                    frames
                WHERE video_id=%s
              """
        cursor.execute(sql, video_object['video_id'])
        frame_data = cursor.fetchall()

        compiled_video_path = os.path.join('static', ''.join(video_object['video_path'].split('.')[:-1]) + '_complied')

        if not os.path.isdir(compiled_video_path):
            os.makedirs(compiled_video_path)

        i = 0
        for frame in frame_data:
            time = i / 30
            frame_name = frame['frame_path'].split('/')[-1]
            
            if frame['mouthwash_use']:
                mouthwash_use_coords = json.loads(frame['mouthwash_use'])
                mouthwash_use_label = 'mouthwash_use'
            else:
                mouthwash_use_coords = None

            if frame['gargling']:
                gargling_coords = json.loads(frame['gargling'])
                gargling_label = 'gargling'
            else:
                gargling_coords = None

            if frame['spitting']:
                spitting_coords = json.loads(frame['spitting'])
                spitting_label = 'spitting'
            else:
                spitting_coords = None
            
            if frame['swishing']:
                swishing_coords = json.loads(frame['swishing'])
                swishing_label = 'swishing'
            else:
                swishing_coords = None

            if frame['rinse']:
                rinse_coords = json.loads(frame['rinse'])
                rinse_label = 'rinse'
            else:
                rinse_coords = None
            
            if frame['product']:
                product_coords = json.loads(frame['product'])
                product_label = 'product'
            else:
                product_coords = None

            if frame['tap_open']:
                tap_open_coords = json.loads(frame['tap_open'])
                tap_open_label = 'tap_open'
            else:
                tap_open_coords = None

            image = cv2.imread(frame['frame_path'])
            shape = image.shape
            thickness = 2
            if shape[1] == 1080:
                font_size = 2
            else:
                font_size = 1
            color = (255, 0, 0)
            font = cv2.FONT_HERSHEY_SIMPLEX

            if font_size == 2:
                image = cv2.putText(image, str(round(time, 2)), (5, 100), font, font_size, color, 2, cv2.LINE_AA)
            else:
                image = cv2.putText(image, str(round(time, 2)), (5, 40), font, font_size, color, 2, cv2.LINE_AA)
            if mouthwash_use_coords:
                start_point = (int(mouthwash_use_coords[0]), int(mouthwash_use_coords[1]))
                end_point = (int(mouthwash_use_coords[2]), int(mouthwash_use_coords[3]))
                image = cv2.rectangle(image, start_point, end_point, color, thickness)
                label_start_point = (start_point[0] + 2, end_point[1] - 5)
                image = cv2.putText(image, mouthwash_use_label, label_start_point, font, font_size, color, 2, cv2.LINE_AA)

            if gargling_coords:
                start_point = (int(gargling_coords[0]), int(gargling_coords[1]))
                end_point = (int(gargling_coords[2]), int(gargling_coords[3]))
                image = cv2.rectangle(image, start_point, end_point, color, thickness)
                label_start_point = (start_point[0] + 2, end_point[1] - 5)
                image = cv2.putText(image, gargling_label, label_start_point, font, font_size, color, 2, cv2.LINE_AA)

            if spitting_coords:
                start_point = (int(spitting_coords[0]), int(spitting_coords[1]))
                end_point = (int(spitting_coords[2]), int(spitting_coords[3]))
                image = cv2.rectangle(image, start_point, end_point, color, thickness)
                label_start_point = (start_point[0] + 2, end_point[1] - 5)
                image = cv2.putText(image, spitting_label, label_start_point, font, font_size, color, 2, cv2.LINE_AA)
            
            if swishing_coords:
                start_point = (int(swishing_coords[0]), int(swishing_coords[1]))
                end_point = (int(swishing_coords[2]), int(swishing_coords[3]))
                image = cv2.rectangle(image, start_point, end_point, color, thickness)
                label_start_point = (start_point[0] + 2, end_point[1] - 5)
                image = cv2.putText(image, swishing_label, label_start_point, font, font_size, color, 2, cv2.LINE_AA)

            if rinse_coords:
                start_point = (int(rinse_coords[0]), int(rinse_coords[1]))
                end_point = (int(rinse_coords[2]), int(rinse_coords[3]))
                image = cv2.rectangle(image, start_point, end_point, color, thickness)
                label_start_point = (start_point[0] + 2, end_point[1] - 5)
                image = cv2.putText(image, rinse_label, label_start_point, font, font_size, color, 2, cv2.LINE_AA)

            if product_coords:
                start_point = (int(product_coords[0]), int(product_coords[1]))
                end_point = (int(product_coords[2]), int(product_coords[3]))
                image = cv2.rectangle(image, start_point, end_point, color, thickness)
                label_start_point = (start_point[0] + 2, end_point[1] - 5)
                image = cv2.putText(image, product_label, label_start_point, font, font_size, color, 2, cv2.LINE_AA)

            if tap_open_coords:
                start_point = (int(tap_open_coords[0]), int(tap_open_coords[1]))
                end_point = (int(tap_open_coords[2]), int(tap_open_coords[3]))
                image = cv2.rectangle(image, start_point, end_point, color, thickness)
                label_start_point = (start_point[0] + 2, end_point[1] - 5)
                image = cv2.putText(image, tap_open_label, label_start_point, font, font_size, color, 2, cv2.LINE_AA)

            new_frame_path = os.path.join(compiled_video_path, frame_name)
            cv2.imwrite(new_frame_path, image)
            i += 1

        print('frames dumped at ', compiled_video_path)

    connection.close()


def make_multiple_videos():
    connection = db_config.get_connection()

    with connection.cursor() as cursor:
        sql = """
                SELECT
                    *
                FROM
                    videos
                WHERE video_id>=204
              """
        cursor.execute(sql)
        data = cursor.fetchall()

    for d in data:
        make_video(d)


if __name__ == "__main__":
    # v_object = {'video_id': 204,
    #             'video_path': 'four_new_videos/1116_-_Cell_2_-_Signal_White_Now_Gold.mp4'}
    # make_video(v_object)
    make_multiple_videos()
