Name:       sailfishos-rotation-fix

# >> macros
BuildArch: armv7hl
# << macros

Summary:    Lock orientation in LandscapeInverted
Version:    0.0.1
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   sailfishsilica-qt5 = 0.20.11.1

%description
Test patch for locking orientation in LandscapeInverted


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfishos-rotation-fix
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfishos-rotation-fix
mkdir -p %{buildroot}/usr/share/jolla-settings/pages/sailfishos-rotation-fix
# << install pre

# >> install post
# << install post

%pre
# >> pre
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u sailfishos-rotation-fix || true
fi
# << pre

%preun
# >> preun
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u sailfishos-rotation-fix || true
fi
# << preun

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfishos-rotation-fix
# >> files
# << files
