#
# api/Makefile ---
#

ifeq (${API_DIR},)
  $(error source ./ht-setup.env first.)
endif

SHELL:=bash
.SUFFIXES:

#####

_default: _ve_build

#####

_apt_get_install:
# For python3
	sudo apt-get install -y python3 python3-venv python3-setuptools python3-wheel

_brew_install:
# For python3 for OSX
	brew install python3
# Use brew pip3 to install packages
	/usr/local/bin/pip3 install wheel setuptools

#####

sys_python3_exe=$(shell PATH=/usr/bin:/usr/local/bin:${PATH} type -p python3)

# check they are set.
ifeq (${sys_python3_exe},)
  $(error the system python3 was not found.)
endif

sys_virtualenv_cmd:=${sys_python3_exe} -m venv

ve_python3_exe:=${API_VE_DIR}/bin/python3
ve_pip3_cmd:=${ve_python3_exe} -m pip

api_install_cmd:=${ve_pip3_cmd} install --editable ${API_DIR}

_ve_build:
# build ve
	${sys_python3_exe} -m venv ${API_DIR}/ve
# pip update
	${ve_pip3_cmd} install --upgrade pip setuptools wheel
# extra packages
	${ve_pip3_cmd} install -r requirements.txt
# install ourselves.
#	${ve_pip3_cmd} install -e .

_ve_rm:
	rm -rf ${API_VE_DIR}

_ve_rebuild: _ve_rm _ve_build

${API_VE_DIR}:
	make _ve_build
