#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : google-pasta
Version  : 0.1.7
Release  : 2
URL      : https://files.pythonhosted.org/packages/7a/4e/c3e35716d57eba02e49b8ad72a744435df1935f189fbc5f47edafb6d4f00/google-pasta-0.1.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/7a/4e/c3e35716d57eba02e49b8ad72a744435df1935f189fbc5f47edafb6d4f00/google-pasta-0.1.7.tar.gz
Summary  : pasta is an AST-based Python refactoring library
Group    : Development/Tools
License  : Apache-2.0
Requires: google-pasta-python = %{version}-%{release}
Requires: google-pasta-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : six

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

%description python3
python3 components for the google-pasta package.


%prep
%setup -q -n google-pasta-0.1.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1561270396
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
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
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
