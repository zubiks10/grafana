import subprocess

# List of YAML files to apply
yaml_files = [
    "grafana-configmap.yaml",
    "grafana-deployment.yaml",
    "grafana-nodeport.yaml",
    "grafana-pv.yaml",
    "grafana-service.yaml"
]

def apply_yaml(file):
    try:
        # Running the kubectl create -f command
        result = subprocess.run(["kubectl", "create", "-f", file], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Successfully applied {file}")
        print(result.stdout.decode("utf-8"))
    except subprocess.CalledProcessError as e:
        print(f"Failed to apply {file}")
        print(e.stderr.decode("utf-8"))

if __name__ == "__main__":
    for yaml_file in yaml_files:
        apply_yaml(yaml_file)
