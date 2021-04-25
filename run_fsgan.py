import ffmpeg
import os
from fsgan.inference.swap import FaceSwapping
from fsgan.criterions.vgg_loss import VGGLoss

weights_dir = './fsgan/weights'

finetune_iterations = 800 
seg_remove_mouth = True 
seg_batch_size = 24 
batch_size = 8 

detection_model = os.path.join(weights_dir, 'v2/WIDERFace_DSFD_RES152.pth')
pose_model = os.path.join(weights_dir, 'shared/hopenet_robust_alpha1.pth')
lms_model = os.path.join(weights_dir, 'v2/hr18_wflw_landmarks.pth')
seg_model = os.path.join(weights_dir, 'v2/celeba_unet_256_1_2_segmentation_v2.pth')
reenactment_model = os.path.join(weights_dir, 'v2/nfv_msrunet_256_1_2_reenactment_v2.1.pth')
completion_model = os.path.join(weights_dir, 'v2/ijbc_msrunet_256_1_2_inpainting_v2.pth')
blending_model = os.path.join(weights_dir, 'v2/ijbc_msrunet_256_1_2_blending_v2.pth')
criterion_id_path = os.path.join(weights_dir, 'v2/vggface2_vgg19_256_1_2_id.pth')
criterion_id = VGGLoss(criterion_id_path)

face_swapping = FaceSwapping(
    detection_model=detection_model, pose_model=pose_model, lms_model=lms_model,
    seg_model=seg_model, reenactment_model=reenactment_model,
    completion_model=completion_model, blending_model=blending_model,
    criterion_id=criterion_id,
    finetune=True, finetune_save=True, finetune_iterations=finetune_iterations,
    seg_remove_mouth=finetune_iterations, batch_size=batch_size,
    seg_batch_size=seg_batch_size, encoder_codec='mp4v')


def encode_audio(video_path, audio_path, output_path):
  ffmpeg.concat(ffmpeg.input(video_path), ffmpeg.input(audio_path), v=1, a=1) \
    .output(output_path, strict='-2').run(overwrite_output=True)

finetune = True
source_path = './data/source.mp4' 
select_source = 'longest' 
target_path = './data/target.mp4'
select_target = 'longest'
output_tmp_path = './data/output_tmp.mp4'
output_path = './output.mp4'


if __name__ == '__main__':
    face_swapping(source_path, target_path, output_tmp_path,
              select_source, select_target, finetune)

    encode_audio(output_tmp_path, target_path, output_path)
    os.remove(output_tmp_path)