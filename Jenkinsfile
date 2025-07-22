pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'abisheak469/python'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_HUB_REPO}:${IMAGE_TAG}")
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_HUB_USER', passwordVariable: 'DOCKER_HUB_PASS')]) {
                    sh """
                        echo "$DOCKER_HUB_PASS" | docker login -u "$DOCKER_HUB_USER" --password-stdin
                    """
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                sh "docker push ${DOCKER_HUB_REPO}:${IMAGE_TAG}"
            }
        }

        stage('Deploy Locally on Jenkins Host') {
            steps {
                script {
                    sh """
                        docker stop flask || true
                        docker rm flask || true
                        docker pull ${DOCKER_HUB_REPO}:${IMAGE_TAG}
                        docker run -d --name flask -p 80:5000 ${DOCKER_HUB_REPO}:${IMAGE_TAG}
                    """
                }
            }
        }
    }
}
