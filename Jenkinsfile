pipeline {
    agent any
    environment {
        DOCKER_CREDENTIALS = credentials('harbor')
        REGISTRY = 'harbor.kube.itdw.io'
        ORG = 'danielwaldmann'
        APP = 'django-rest'
        BUILDVERSION = sh(script: "date +%Y-%m-%d-%H-%M", returnStdout: true).trim()
        RECIPIENT = 'daniel@dwaldmann.de'
    }
    stages {
        stage('Init') {
            steps {
                echo 'Initializing ...'
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                echo "Current branch: ${env.BRANCH_NAME}"
                sh 'docker login -u $DOCKER_CREDENTIALS_USR -p $DOCKER_CREDENTIALS_PSW ${REGISTRY}'
            }
        }
        stage('Build & Publish') {
            steps {
                echo 'Building and Publishing image to Registry ...'
                sh 'docker buildx create --use && docker buildx build --pull --push --no-cache --platform linux/amd64,linux/arm64 --tag ${REGISTRY}/${ORG}/${APP}:latest --tag ${REGISTRY}/${ORG}/${APP}:${BUILDVERSION} .'
            }
        }
        stage('Cleanup') {
            steps {
                echo 'Cleaning up ...'
                cleanWs()
            }
        }
    }
    post {
        always {
            emailext to: "${RECIPIENT}",
            subject: "Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}",
            body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}",
            attachLog: true
        }
    }
}