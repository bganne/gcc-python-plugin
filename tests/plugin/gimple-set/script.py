#   Copyright 2015 Benoit Ganne <benoit.ganne@gmail.com>
#
#   This is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see
#   <http://www.gnu.org/licenses/>.

# Verify examining details of functions

import gcc
from gccutils import pprint

class GimpleSet(gcc.GimplePass):
	def execute(self, fun):
		if fun and fun.decl.name == "main":
			for bb in fun.cfg.basic_blocks:
				for i in range(len(bb.gimple)):
					if str(bb.gimple[i]) == "ret = -1;":
						bb.gimple = bb.gimple[:i] + bb.gimple[i+1:]
						return


ps = GimpleSet(name='gimple-set-test')
ps.register_after('cfg')
