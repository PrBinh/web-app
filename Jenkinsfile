pipeline {
   agent any
   stages {
       stage('Build') {
           agent {
               docker {
                   image 'python:3.6'
               }
	   }
           steps {
		// install requirements package
		sh 'pip install -r ./app/requirements.txt'
		sh 'python main.py'
               // Build docker image file
               sh 'docker build -f ./docker/Dockerfile -t hello-python:latest .'          
           }    
       }
       stage('Test') {
           agent {
               docker {
                   image 'python:3.6'
               }
	   }
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
