pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from Git repository
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/Chandrahasa3008/CalculatorApplication.git']]])
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image using the Dockerfile
                script {
                    docker.build('my-custom-image:latest', '.')
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                // Run the Docker container
                script {
                    docker.image('my-custom-image:latest').run('-v /var/run/docker.sock:/var/run/docker.sock', '--rm')
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker containers after execution
            script {
                docker.image('my-custom-image:latest').inside {
                    sh 'echo Clean up steps or additional cleanup commands here'
                }
            }
        }
    }
}
