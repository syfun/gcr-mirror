image_list_str = """
k8s.gcr.io/kube-apiserver:v1.16.1
k8s.gcr.io/kube-controller-manager:v1.16.1
k8s.gcr.io/kube-scheduler:v1.16.1
k8s.gcr.io/kube-proxy:v1.16.1
k8s.gcr.io/pause:3.1
k8s.gcr.io/etcd:3.3.15-0
k8s.gcr.io/coredns:1.6.2
"""
import os


def get_images(image_list_str):
    images = image_list_str.strip().split()

    return [image.replace("k8s.gcr.io/", "").split(":") for image in images]


base_dir = os.path.dirname(os.path.abspath(__name__))

for image in image_list_str.strip().split():
    image_name, image_tag = image.replace("k8s.gcr.io/", "").split(":")
    image_dir = os.path.join(base_dir, image_name, image_tag)
    try:
    	os.mkdir(image_dir)
    except FileExistsError:
    	pass

    with open(os.path.join(image_dir, "Dockerfile"), "w") as f:
        f.write(f"FROM {image}\n")
