
node("docker-test") {
    checkout scm

    stage("Unit Test") {
      sh "docker stop hello_app || true                       "
      sh "docker rm hello_app || true                         "
      sh "docker build -t my_build .                          "
      sh "docker run -p 8888:8888 -d --name hello_app my_build"

    }
    stage("Integration Test") {
      try {
        sh "docker build -t cd-demo ."
        sh "docker rm -f cd-demo || true"
        sh "docker run -d -p 8080:8080 --name=cd-demo cd-demo"
        // env variable is used to set the server where go test will connect to run the test
        sh "docker run --rm -v ${WORKSPACE}:/go/src/cd-demo --link=cd-demo -e SERVER=cd-demo golang go test cd-demo -v --run Integration"
      }
      catch(e) {
        error "Integration Test failed"
      }finally {
        sh "docker rm -f hello_app || true"
      }
    }
    stage("Build") {
      sh "echo dockertest build"
    }
    stage("Publish") {
      sh "echo dockertest publish"
    }
  }