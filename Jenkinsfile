node {
   stage('Build') {
      sh "cd docker"
      sh "docker build -t web:v1 ."
      sh "cd ../k8s"
      sh "docker build -t api:v1 -f Dockerfile.flask ."
      sh "docker build -t db:v1 -f Dockerfile.mongo ."
   }
   stage('Results') {
      sh 'echo done'
   }
}