
node("build") {
	checkout scm
	stage("Build") {
		sh "docker stop hello_unit || true                       "
		sh "docker rm hello_unit || true                         "
		sh "docker build -t hello_unit .                          "
		sh "docker run -p 8888:8888 -d --name hello_unit hello_unit"
	}
}
node("test") {
	stage("Unit Test") {
		sh "docker stop hello_test || true                       "
		sh "docker rm hello_test || true                         "
		sh "docker build -t hello_test .                          "
		sh "docker run -p 8888:8888 -d --name hello_test hello_test"
	}
}
node("prod") {
	stage("Deploy") {
		try {
			sh "docker stop hello_prod || true                       "
			sh "docker rm hello_prod || true                         "
			sh "docker build -t hello_prod .                          "
			sh "docker run -p 8888:8888 -d --name hello_prod hello_prod"
		}
		catch(e) {
			error "deployment error - heal"
		}
	}
}