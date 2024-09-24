Installing Grafana in a Kubernetes (K8s) cluster from scratch involves a series of steps. Below is a detailed guide to help you get Grafana up and running.

### Prerequisites

1. **Kubernetes Cluster**: Ensure you have access to a Kubernetes cluster (e.g., using Minikube, GKE, EKS, AKS, or any other K8s service).
2. **kubectl**: The Kubernetes command-line tool should be installed and configured to communicate with your cluster.
3. **Helm (Optional)**: If you prefer using Helm for installation, make sure it is installed.

### Step 1: Create a Namespace (Optional)

It’s a good practice to create a dedicated namespace for Grafana:

```bash
kubectl create namespace grafana
```

### Step 2: Install Grafana Using Helm

Helm simplifies the installation process. If you don't have Helm installed, 
follow the [Helm installation guide](https://helm.sh/docs/intro/install/).

1. **Add the Grafana Helm Repository**:

   ```bash
   helm repo add grafana https://grafana.github.io/helm-charts
   helm repo update
   ```

2. **Install Grafana**:

   You can customize the installation with various options. Here’s a basic installation command:

   ```bash
   helm install grafana grafana/grafana --namespace grafana --set admin.password='YourStrongPassword'
   ```

   Replace `YourStrongPassword` with a secure password for the Grafana admin user.

### Step 3: Verify the Installation

Check the status of the Grafana pod to ensure it’s running:

```bash
kubectl get pods -n grafana
```

You should see a pod named something like `grafana-<random-string>` in the `Running` state.

### Step 4: Access Grafana

#### a. Port Forwarding

You can use port forwarding to access Grafana locally:

```bash
kubectl port-forward svc/grafana 3000:80 -n grafana
```

Now, open your browser and navigate to [http://localhost:3000](http://localhost:3000).

#### b. LoadBalancer Service (Optional)

If you want to expose Grafana externally and your cluster supports LoadBalancer services, you can modify the service type:

```bash
kubectl patch svc grafana -n grafana -p '{"spec": {"type": "LoadBalancer"}}'
```

Check for the external IP:

```bash
kubectl get svc -n grafana
```

You can then access Grafana at `http://<external-ip>:80`.

### Step 5: Log In to Grafana

- **Username**: `admin`
- **Password**: The password you set in Step 2.

### Step 6: Set Up a Data Source

1. Once logged in, go to the gear icon on the left sidebar and select **Data Sources**.
2. Choose the data source you want to configure (e.g., Prometheus).
3. Fill in the required details, such as the URL of your Prometheus instance.
4. Click **Save & Test** to check the connection.

### Step 7: Create a Dashboard

1. Click on the **+** icon on the left sidebar and select **Dashboard**.
2. Add a new panel and select the data source you configured earlier.
3. Create queries to visualize your data.

### Step 8: (Optional) Configure Persistent Storage

If you want to retain Grafana data across pod restarts, you can configure persistent storage. Here's how to do it:

1. Create a PersistentVolumeClaim (PVC):

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: grafana-pvc
  namespace: grafana
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
```

Apply it:

```bash
kubectl apply -f grafana-pvc.yaml
```

2. Update the Helm installation to use the PVC:

```bash
helm upgrade grafana grafana/grafana --namespace grafana --set persistence.enabled=true --set persistence.existingClaim=grafana-pvc
```

### Conclusion

You have successfully installed Grafana in your Kubernetes cluster. You can now configure it, create dashboards, and visualize your metrics. If you have any specific requirements or run into issues, feel free to ask!# grafana
