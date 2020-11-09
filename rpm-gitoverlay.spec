Name:           rpm-gitoverlay
Version:        0
Release:        1%{?dist}
Summary:        Manage an overlay repository of RPMs from upstream git

License:        GPLv3+
URL:            https://github.com/ignatenkobrain/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python-nose
BuildRequires:  python-marshmallow
#BuildRequires:  python-marshmallow-enum
BuildRequires:  rpm-python
BuildRequires:  python2-pyyaml
BuildRequires:  git-core
Requires:       python-marshmallow
#Requires:       python-marshmallow-enum
Requires:       rpm-python
Requires:       python2-pyyaml
Requires:       git-core
# Archives are always in tar.xz
Requires:       /usr/bin/tar
Requires:       /usr/bin/xz
# For building SRPMs
Requires:       /usr/bin/rpmbuild
# COPR builder
Requires:       python-beautifulsoup4
Requires:       python2-copr
Requires:       python-requests

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup

%build
%py2_build

%install
%py2_install

%check
%{__python2} setup.py test

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{python2_sitelib}/rpm_gitoverlay-*.egg-info/
%{python2_sitelib}/rgo/

%changelog
* Sun Jul 10 2016 Igor Gnatenko <ignatenko@redhat.com> - 0-1
- Initial package
