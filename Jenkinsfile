pipeline {
    agent any

    triggers {
            GenericTrigger(
                genericVariables: [
                    [key: 'WEBHOOK_TRIGGER', value: '$.trigger', defaultValue: '']
                ],
                causeString: 'Triggered by webhook',
                token: 'dodat',
                printContributedVariables: true,
                printPostContent: true
            )
        }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/derricky2004/MLOps_Jenkins.git'
            }
        }
        stage('Run FastAPI Application') {
            steps {
                script {
                    try {
                        sh '''
                        #!/bin/bash

                        # Check if the container already exists
                        if docker ps -a --format '{{.Names}}' | grep -q "^api_running$"; then
                            echo "Container 'api_running' already exists. Removing it..."
                            docker stop api_running
                            docker rm -f api_running
                        fi

                        # Remove existing Docker image
                        if docker images | grep -q "api"; then
                            echo "Removing existing Docker image..."
                            docker rmi -f api
                        fi

                        # Build and run the FastAPI container
                        echo "Building the Docker image..."
                        docker build -t api .

                        echo "Running the Docker container..."
                        docker run --name api_running -p 8001:8001 -d api
                        '''

                        withChecks('Run FastAPI App') {
                            publishChecks name: 'Run FastAPI App', status: 'COMPLETED', conclusion: 'SUCCESS',
                                         summary: 'FastAPI container built and running successfully.'
                        }
                    } catch (e) {
                        withChecks('Run FastAPI App') {
                            publishChecks name: 'Run FastAPI App', status: 'COMPLETED', conclusion: 'FAILURE',
                                         summary: 'Pipeline failed while running the FastAPI container.'
                        }
                        throw e
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 test_main.py'
            }
        }
    }
    post {
        always {
            echo 'Pipeline complete'
        }
    }
}
