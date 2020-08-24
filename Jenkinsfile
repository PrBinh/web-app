pipeline {
   agent any
   stages {
       stage('Build') {
           agent any
           steps {
				// install requirements package
			   sh 'pip install -r requirements.txt'
			   sh 'python main.py'
               // Build docker image file
               sh 'docker build -f Dockerfile -t hello-python:latest .'          
           }    
       }
       stage('Test') {
           agent any
           steps {                
               // Run docker with image
               sh 'docker run -p 5001:5000 hello-python'
           }
       }
       stage('Publish') {
           environment {
               registryCredential = 'dockerhub'
           }
           steps{
               script {
                   def appimage = docker.build registry + ":$BUILD_NUMBER"
                   docker.withRegistry( '', registryCredential ) {
                       appimage.push()
                       appimage.push('latest')
                   }
               }
           }
       }
       stage ('Deploy') {
           steps {
               script{
                   def image_id = registry + ":$BUILD_NUMBER"
                   sh "ansible-playbook  deployment.yml --extra-vars \"image_id=${image_id}\""
               }
           }
       }
   }
}
