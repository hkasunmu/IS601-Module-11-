# IS601 Module 11 Reflection

For Module 11, I learned how to create and test a Calculation model using SQLAlchemy, Pydantic, and PostgreSQL. This assignment was challenging at first because I was still trying to understand how everything from the previous modules connected. However, working through each step helped me understand the process better.

One of the things I learned was how to create a Calculation model that stores numbers, calculation types, and results in a database. I also learned how to use Pydantic to check information before allowing it into the system. For example, I added validation to prevent users from dividing by zero or entering an invalid calculation type.

I also worked with the Factory Pattern, which helped organize the different math operations. Another important part of this assignment was writing tests to make sure the calculations worked correctly.

One challenge I experienced was getting PostgreSQL to connect properly. My previous Module 9 Docker container was already using the same port, which caused an error. I had to change the port and configure my environment variables before getting the database running. I also had some issues with my integration tests, but I was able to resolve them.

After making these corrections, I successfully ran all 22 tests locally. I also configured GitHub Actions for automated testing and Docker Hub deployment. I also configured GitHub Actions to automatically run my tests, scan the Docker image, and deploy it to Docker Hub. At first, GitHub Actions was experiencing delays, which made me think something was wrong with my project. However, the workflows eventually ran successfully, and I was able to confirm that my Docker image was published. This helped me better understand how automated testing and deployment work together.

Overall, this assignment helped me become more comfortable with Python testing, database models, Docker, and CI/CD. Although I faced challenges, I learned more about identifying errors and correcting them instead of starting everything over.