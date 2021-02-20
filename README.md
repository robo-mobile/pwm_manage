# pwm manage

**pwm manage** - this is a separate software module needed to control GPIO RPI

## Install

```shell script
pip install .
```

## Online help

pwm manage provide an online help:
```shell script
# pwm help
Usage: pwm command [options]

Commands:
    help    -- Show help
    engines -- number of engines: 4 (choose 2 or 4)
    w-time  -- time of execution of one command (in seconds)
    power   -- the power of the motors (in percent)
```

### Example: 
```shell script
# start driver
pwm start

# send test signals
pwm test --engines 4 --w-time 1 --power 25
```

## Deployment 

Read more about deployment in  [deploy](./deploy/README.md) documentation.
