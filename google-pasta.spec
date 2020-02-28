#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : google-pasta
Version  : 0.1.8
Release  : 9
URL      : https://files.pythonhosted.org/packages/57/ac/aebe06c6a3154ce21fe82d42f31511ababe87dc30c1b041716493e061633/google-pasta-0.1.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/57/ac/aebe06c6a3154ce21fe82d42f31511ababe87dc30c1b041716493e061633/google-pasta-0.1.8.tar.gz
Summary  : pasta is an AST-based Python refactoring library
Group    : Development/Tools
License  : Apache-2.0
Requires: google-pasta-python = %{version}-%{release}
Requires: google-pasta-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : six
BuildRequires : util-linux

%description
# pasta: **P**ython **AST** **A**ugmentation
*This is still a work-in-progress; there is much more to do. Existing
functionality may not be perfect.*

%package python
Summary: python components for the google-pasta package.
Group: Default
Requires: google-pasta-python3 = %{version}-%{release}

%description python
python components for the google-pasta package.


%package python3
Summary: python3 components for the google-pasta package.
Group: Default
Requires: python3-core
Provides: pypi(google-pasta)

%description python3
python3 components for the google-pasta package.


%prep
%setup -q -n google-pasta-0.1.8
cd %{_builddir}/google-pasta-0.1.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582931713
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
