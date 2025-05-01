pipeline {
    agent {
        docker {
            image 'python:3.8'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                    echo "Installing dependencies..."
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh '''
                    echo "Running build script..."
                    chmod +x build.sh
                    ./build.sh
                    '''
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    sh '''
                    echo "Running application..."
                    chmod +x run.sh
                    ./run.sh
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh '''
                    echo "Running tests..."
                    chmod +x test.sh
                    ./test.sh
                    '''
                }
            }
        }
    }

    post {
        success {
            echo '🎉 CI Pipeline completed successfully!'
        }
        failure {
            echo '💥 Something went wrong in the pipeline!'
        }
    }
}
