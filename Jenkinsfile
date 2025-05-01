pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo '🔨 Building the application...'
                sh 'echo "Build step executed"'
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running tests...'
                sh 'echo "Test step executed"'
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploying application...'
                sh 'echo "Deploy step executed"'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline executed successfully!'
            echo '📜 Displaying Menu Output Below:'
          
        }
        failure {
            echo '💥 Something went wrong in the pipeline!'
        }
    }
}
