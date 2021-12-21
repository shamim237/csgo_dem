from datetime import timedelta
import cv2
import numpy as np
import os
import glob


img_dim  = [180,80]

images = []
SAVING_FRAMES_PER_SECOND = 16       # The required fps for frames extraction

def format_timedelta(td):
    
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        result = result + ".00"
        return result.replace(":", "-")

    ms = int(ms)
    ms = round(ms / 1e4)

    return f"{result}.{ms:02}".replace(":", "-")


def get_saving_frames_durations(cap, saving_fps):
    """A function that returns the list of durations where to save the frames"""
    s = []
    # get the clip duration by dividing number of frames by the number of frames per second
    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
    # use np.arange() to make floating-point steps
    for i in np.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s


def main(video_file):

    videoname = os.path.basename(video_file)
    videoname = videoname.split(".")[0]

    filename = "all_frames"
    # # make a folder by the name of the video file
    if not os.path.isdir(filename):
        os.mkdir(filename)

    #read the video file    
    cap = cv2.VideoCapture(video_file)
    # get the FPS of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    # if the SAVING_FRAMES_PER_SECOND is above video FPS, then set it to FPS (as maximum)
    saving_frames_per_second = min(fps, SAVING_FRAMES_PER_SECOND)
    # get the list of duration spots to save
    saving_frames_durations = get_saving_frames_durations(cap, saving_frames_per_second)
    # start the loop
    count = 0

    while True:

        if count >= 9899:
          break
        is_read, frame = cap.read()
        if not is_read:
            # break out of the loop if there are no frames to read
            break
        # get the duration by dividing the frame count by the FPS
        frame_duration = count / fps
        try:
            # get the earliest duration to save
            closest_duration = saving_frames_durations[0]
        except IndexError:
            # the list is empty, all duration frames were saved
            break
        if frame_duration >= closest_duration:
            # if closest duration is less than or equals the frame duration, 
            # then save the frame
            frame_duration_formatted = format_timedelta(timedelta(seconds=frame_duration))
             
            # drop the duration spot from the list, since this duration spot is already saved
            # img = crop_center_square(frame)
            frame = frame[192 : 192 + 488, 378 : 378 + 800]
            img = cv2.resize(frame, (img_dim[0], img_dim[1]))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            xx = videoname + "_" + str(frame_duration_formatted) + ".png"

            # cv2.imwrite(os.path.join(filename, xx), img)

            print(xx, file = open("/media/opus-bot-team/Ubuntu Works/OpusTech_Ubuntu/action_sync/all_csv/all_frames.txt", "a"))
            # images.append(img)

            try:
                saving_frames_durations.pop(0)
            except IndexError:
                pass
        # increment the frame count
        count += 1

    print(xx)



if __name__ == "__main__":

    for video_file in sorted(glob.glob("/media/opus-bot-team/Ubuntu Works/OpusTech_Ubuntu/action_sync/videos/*.mp4")):

        main(video_file)

