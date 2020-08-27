pipeline {
   agent any
   environment {
       registry = "binhdocker/webapp"
       GOCACHE = "/tmp"
   }
   stages {
       stage('Build') {
           agent {
               docker {
                   image 'golang'
               }
           }
           steps {
               // Create our project directory.
               //sh 'cd ./'
               //sh 'mkdir -p webapp'
               // Copy all files in our Jenkins workspace to our project directory.               
               //sh 'cp -r ${WORKSPACE}/* webapp'
               // Build the app.
               sh 'go build'              
           }    
       }
       stage('Test') {
           agent {
               docker {
                   image 'golang'
               }
           }
           steps {                
               // Create our project directory.
               //sh 'cd ${GOPATH}/src'
               //sh 'mkdir -p webapp'
               // Copy all files in our Jenkins workspace to our project directory.               
               //sh 'cp -r ${WORKSPACE}/* webapp'
               // Remove cached test results.
               sh 'go clean -cache'
               // Run Unit Tests.
               sh 'go test ./... -v -short'           
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
                   sh "ansible-playbook  playbook.yml  --extra-vars \"image_id=${image_id}\""
               }
           }
       }
   }
}
