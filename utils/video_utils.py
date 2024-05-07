import cv2

def read_video(video_path,sample_rate):
    cap = cv2.VideoCapture(video_path)
    sampled_frames = []
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Process only every 'sample_rate'th frame
        if frame_count % sample_rate == 0:
            sampled_frames.append(frame)

        frame_count += 1

    cap.release()
    return sampled_frames

def save_video(ouput_video_frames,output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (ouput_video_frames[0].shape[1], ouput_video_frames[0].shape[0]))
    for frame in ouput_video_frames:
        out.write(frame)
    out.release()
