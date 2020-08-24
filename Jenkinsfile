pipeline {
   agent any
   stages {
       stage('Build') {
           agent {
               docker {
                   image 'python'
               }
           }
           steps {
               // Build docker image file
               sh 'docker build -f Dockerfile -t hello-python:latest'          
           }    
       }
       stage('Test') {
           agent {
               docker {
                   image 'python'
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
                   sh "ansible-playbook  playbook.yml --extra-vars \"image_id=${image_id}\""
               }
           }
       }
   }
}
