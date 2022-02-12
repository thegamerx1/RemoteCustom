function script_path()
   local str = debug.getinfo(2, "S").source:sub(2)
   return str:match("(.*[/\\])")
end


function action(val)
	return "\""..script_path().."program.exe\" "..val
end

actions.locko = function ()
	os.execute(action("locko"))
end

actions.screenson = function ()
	os.execute(action("screenson"))
end

actions.screensoff = function ()
	os.execute(action("screensoff"))
end

actions.animexd = function ()
	os.execute(action("animexd"))
end
