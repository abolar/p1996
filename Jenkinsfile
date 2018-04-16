
node("build") {
	checkout scm
	
	stage("Build") {
		sh "docker stop hello_unit || true                         "
		sh "docker rm hello_unit || true                           "
		sh "docker build -f DockerfileBuild -t hello_unit .        "
		sh "docker run -p 8888:8888 -d --name hello_unit hello_unit"
	}
}
node("build")  {
	stage("Unit Test") {
		sh "/home/abolar/.local/bin/pytest unit_test.py"
	}
}
node("test")  {
	stage("Integration Test") {
		sh "docker stop hello_test || true                         "
		sh "docker rm hello_test || true                           "
		sh "docker build -f DockerfileTest -t hello_test .         "
		sh "docker run -p 8889:8888 -d --name hello_test hello_test"
		sh "/home/abolar/.local/bin/pytest unit_test.py"
	}
}
node("prod")  {
	stage("Deploy") {
		try {
			sh "docker stop hello_prod || true                         "
			sh "docker rm hello_prod || true                           "
			sh "docker build -f DockerfileProd -t hello_prod .         "
			sh "docker run -p 8890:8888 -d --name hello_prod hello_prod"
		}
		catch(e) {
			error "deployment error - heal"
		}
	}
}