import xml.etree.ElementTree as ET
import os


def convert_annotation(annotation_path, image_id, list_file, classes):
    in_file = open(annotation_path + '%s.xml' % image_id)
    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))


def conver_to_train_list_txt(annotation_path, image_path, classes, output_file_dir):

    xml_names = os.listdir(annotation_path)
    image_ids = [xml_name[0:-4] for xml_name in xml_names]
    list_file = open(output_file_dir + 'train_list.txt', 'w')
    for image_id in image_ids:
        list_file.write('%s%s.png' % (image_path, image_id))
        convert_annotation(annotation_path, image_id, list_file, classes)
        list_file.write('\n')
    list_file.close()


"""xml_file_path为标注后的XML文件路径，image_path为所标注的图片的路径（该路径下图片数量与标记数量要一致），
output_txtfile_dir为输出的trainlist文件的路径，该文件包含了image的路径的bbox信息。"""

xml_file_path = 'D:/hat_mask_detection/kitchen_data/annotations/'
image_path = 'D:/hat_mask_detection/kitchen_data/train_image/'
classes = ["head"]
output_txtfile_dir = 'D:/hat_mask_detection/'

conver_to_train_list_txt(xml_file_path, image_path, classes, output_txtfile_dir)

