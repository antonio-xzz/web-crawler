.PHONY: install-pyenv-bash
install-pyenv-bash: ## Installs pyenv on bash shell
	curl https://pyenv.run | bash
	echo 'export PYENV_ROOT="$$HOME/.pyenv"' >> ~/.bashrc
	echo 'export PATH="$$PYENV_ROOT/bin:$$PATH"' >> ~/.bashrc
	echo 'eval "$$(pyenv init -)"' >> ~/.bashrc
	exec "$$SHELL"

.PHONY: install-pyenv-zsh
install-pyenv-zsh: ## Installs pyenv on zsh shell
	curl https://pyenv.run | zsh
	echo 'export PYENV_ROOT="$$HOME/.pyenv"' >> ~/.zshrc
	echo 'export PATH="$$PYENV_ROOT/bin:$$PATH"' >> ~/.zshrc
	echo 'eval "$$(pyenv init -)"' >> ~/.zshrc
	exec "$$SHELL"

.PHONY: install-requirements
install-requirements: ## Installs all the requirements
	pyenv install 3.12
	pyenv global 3.12
	pip install poetry
	poetry install

.PHONY: activate
activate: ## Activate the virtual environment
	poetry shell

.PHONY: run
run: ## Runs the project
	cd app && uvicorn main:app --reload

.PHONY: pytest
pytest: ## Runs the tests for the project
	poetry run pytest -s -v $(test)
